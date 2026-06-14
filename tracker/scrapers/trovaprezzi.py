"""Scraper per trovaprezzi.it — usa API price_chart + HTML per offerte."""

import http.cookiejar
import json
import re
import sys
import urllib.parse
import urllib.request
import urllib.error
from .base import extract_jsonld, parse_price_eu, find_prices_in_text


_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/148.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
    "Accept-Encoding": "identity",
    "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", '
                 '"Not/A)Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}


def _create_session():
    """Crea un opener con cookie jar per mantenere la sessione."""
    jar = http.cookiejar.CookieJar()
    return urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(jar)
    ), jar


def _session_fetch(opener, url: str, headers: dict | None = None,
                   timeout: int = 15) -> str:
    """Fetch con session/cookie, ritorna HTML."""
    hdrs = headers or _HEADERS
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with opener.open(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} per {url}", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"Errore fetch {url}: {e}", file=sys.stderr)
        return ""


def _extract_csrf(html: str) -> str | None:
    """Estrae il CSRF token dal meta tag nella pagina HTML."""
    m = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', html)
    return m.group(1) if m else None


def _extract_slug(url: str) -> str | None:
    """Estrae lo slug prodotto dall'URL trovaprezzi.

    Es: /televisori-lcd-plasma/prezzi-scheda-prodotto/samsung_qn85f_55_qe55qn85fauxzt-v
    → samsung_qn85f_55_qe55qn85fauxzt
    """
    m = re.search(r'/prezzi-scheda-prodotto/([^/?#]+)', url)
    if not m:
        return None
    slug = m.group(1)
    # Rimuovi suffisso variante "-v"
    slug = re.sub(r'-v\d*$', '', slug)
    return slug


def fetch_price_history(slug: str, current_price: float | None = None,
                        csrf_token: str | None = None,
                        opener=None) -> dict | None:
    """Chiama l'API price_chart per lo storico prezzi.

    Ritorna dict con: data (lista {time, value}), statistics.
    I prezzi sono in EUR (float).
    """
    price_param = f"?current_price={current_price}" if current_price else ""
    url = f"https://www.trovaprezzi.it/price_chart/{slug}{price_param}"

    headers = {
        **_HEADERS,
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"https://www.trovaprezzi.it/televisori-lcd-plasma/"
                   f"prezzi-scheda-prodotto/{slug}-v",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
    }
    if csrf_token:
        headers["X-CSRF-Token"] = csrf_token

    if opener is None:
        opener, _ = _create_session()

    raw = _session_fetch(opener, url, headers=headers)
    if not raw:
        return None

    # Estrai priceTrendsDataSet dal JS
    m = re.search(r'priceTrendsDataSet\s*=\s*(\[.*?\])\s*[,;]', raw, re.DOTALL)
    if not m:
        return None

    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError:
        return None

    if not data:
        return None

    values = [p["value"] for p in data if "value" in p]
    return {
        "slug": slug,
        "data": data,
        "statistics": {
            "lowest": min(values),
            "highest": max(values),
            "average": round(sum(values) / len(values), 2),
            "points": len(values),
        },
    }


def scrape_product(url: str) -> dict:
    """Scrapa una pagina prodotto trovaprezzi.it con sessione + API."""
    opener, jar = _create_session()
    slug = _extract_slug(url)

    result = {
        "url": url,
        "site": "trovaprezzi",
        "price": None,
        "title": None,
        "offers": [],
        "offer_count": 0,
        "slug": slug,
        "price_history": None,
    }

    # 1) Fetch HTML pagina principale (stabilisce sessione + cookie DataDome)
    html = _session_fetch(opener, url)
    if not html:
        result["error"] = "fetch_failed"
        return result

    # Titolo
    m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.DOTALL)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        title = title.split("\n")[0].strip()  # Solo prima riga
        import html as html_mod
        result["title"] = html_mod.unescape(title)

    # "a partire da XX,XX €"
    m = re.search(r'a partire da\s*([\d.,]+)\s*€', html, re.IGNORECASE)
    if m:
        result["price"] = parse_price_eu(m.group(1))

    # JSON-LD
    if result["price"] is None:
        for ld in extract_jsonld(html):
            if not isinstance(ld, dict):
                continue
            offers = ld.get("offers", {})
            if isinstance(offers, dict):
                low = offers.get("lowPrice")
                if low:
                    result["price"] = parse_price_eu(str(low))
                count = offers.get("offerCount")
                if count:
                    result["offer_count"] = int(count)
                if ld.get("name"):
                    result["title"] = ld["name"]

    # Fallback: "lowPrice" raw
    if result["price"] is None:
        m = re.search(r'"lowPrice"\s*:\s*"?([\d.,]+)"?', html)
        if m:
            result["price"] = parse_price_eu(m.group(1))

    # Estrai offerte individuali
    for om in re.finditer(
        r'class="[^"]*merchant_name[^"]*"[^>]*>\s*(.*?)\s*</.*?'
        r'([\d.,]+)\s*(?:€|&euro;)',
        html, re.DOTALL
    ):
        shop = re.sub(r'<[^>]+>', '', om.group(1)).strip()
        price = parse_price_eu(om.group(2))
        if shop and price:
            result["offers"].append({"shop": shop, "price": price})

    # Ultimo fallback prezzi
    if result["price"] is None:
        prices = find_prices_in_text(html, min_price=50)
        if prices:
            result["price"] = min(prices)

    # 2) API price_chart — storico prezzi (usa la sessione stabilita)
    if slug:
        csrf = _extract_csrf(html)
        history = fetch_price_history(
            slug, current_price=result["price"],
            csrf_token=csrf, opener=opener
        )
        if history:
            result["price_history"] = {
                "lowest": history["statistics"]["lowest"],
                "highest": history["statistics"]["highest"],
                "average": history["statistics"]["average"],
            }

    return result


def search_product(query: str) -> list[dict]:
    """Cerca un prodotto su trovaprezzi.it."""
    search_url = (f"https://www.trovaprezzi.it/prezzi_televisori-lcd-plasma"
                  f".aspx?libera={urllib.parse.quote(query)}")
    opener, _ = _create_session()
    html = _session_fetch(opener, search_url)
    if not html:
        return []

    results = []
    for m in re.finditer(
        r'<a[^>]*href="(https://www\.trovaprezzi\.it/[^"]*'
        r'prezzi-scheda-prodotto[^"]*)"[^>]*>.*?'
        r'([\d.,]+)\s*(?:€|&euro;)',
        html, re.DOTALL
    ):
        url = m.group(1)
        price = parse_price_eu(m.group(2))
        slug = url.split("/")[-1].replace("-v", "").replace("-", " ").replace("_", " ")
        if price:
            results.append({
                "url": url,
                "title": slug,
                "price": price,
                "site": "trovaprezzi",
            })
            if len(results) >= 5:
                break

    return results
