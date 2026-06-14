"""Scraper per Amazon EU — usa API twister + HTML fallback."""

import json
import re
import urllib.parse
from .base import fetch, extract_jsonld, parse_price_eu, find_prices_in_text

# Domini Amazon EU con priorità Italia-first
DOMAINS = {
    "it": "www.amazon.it",
    "de": "www.amazon.de",
    "fr": "www.amazon.fr",
    "es": "www.amazon.es",
    "nl": "www.amazon.nl",
    "be": "www.amazon.com.be",
    "pl": "www.amazon.pl",
    "se": "www.amazon.se",
    "uk": "www.amazon.co.uk",
}


def extract_asin(url: str) -> str | None:
    """Estrae l'ASIN da un URL Amazon."""
    m = re.search(r'/(?:dp|gp/product|ASIN)/([A-Z0-9]{10})', url)
    return m.group(1) if m else None


def product_url(asin: str, domain: str = "www.amazon.it") -> str:
    return f"https://{domain}/dp/{asin}"


def _fetch_twister_price(asin: str, domain: str = "www.amazon.it") -> dict | None:
    """Chiama l'API twister per ottenere prezzo e disponibilita via JSON.

    L'API twisterDimensionSlotsDefault ritorna JSON strutturato con:
    - twisterSlotJson.price (float, gia in EUR)
    - twisterSlotJson.isAvailable (bool)
    """
    url = (
        f"https://{domain}/gp/product/ajax/twisterDimensionSlotsDefault"
        f"?isDimensionSlotsAjax=1&asinList={asin}&asin={asin}"
        f"&deviceType=web&showFancyPrice=false"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,*/*",
        "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
        "Accept-Encoding": "identity",
        "Referer": f"https://{domain}/dp/{asin}",
    }
    raw = fetch(url, headers=headers, timeout=10)
    if not raw:
        return None

    # Il formato e "streaming JSON" separato da "&&&"
    for chunk in raw.split("&&&"):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            data = json.loads(chunk)
        except json.JSONDecodeError:
            continue
        if not isinstance(data, dict):
            continue
        if data.get("ASIN") != asin:
            continue
        value = data.get("Value", {})
        content = value.get("content", {})
        if isinstance(content, str):
            try:
                content = json.loads(content)
            except json.JSONDecodeError:
                continue
        slot = content.get("twisterSlotJson", {})
        if slot.get("price"):
            return {
                "price": float(slot["price"]),
                "available": slot.get("isAvailable", False),
            }
    return None


def scrape_product(url: str) -> dict:
    """Scrapa una singola pagina prodotto Amazon (API twister + HTML fallback)."""
    asin = extract_asin(url)
    domain = "www.amazon.it"
    m = re.search(r'https?://([^/]+)', url)
    if m:
        domain = m.group(1)

    result = {
        "url": url,
        "site": "amazon",
        "price": None,
        "title": None,
        "availability": None,
        "seller": None,
        "asin": asin,
    }

    # 1) API twister — fonte primaria per il prezzo (JSON strutturato)
    if asin:
        twister = _fetch_twister_price(asin, domain)
        if twister:
            result["price"] = twister["price"]
            # Nota: twister isAvailable indica se la variante/dimensione e
            # selezionabile, NON se il prodotto e in stock. La disponibilita
            # reale viene determinata dall'HTML della pagina prodotto.

    # 2) HTML — per titolo, venditore, disponibilita e prezzo fallback
    html = fetch(url)
    if html:
        # Titolo
        tm = re.search(r'id="productTitle"[^>]*>\s*(.*?)\s*<', html, re.DOTALL)
        if tm:
            result["title"] = tm.group(1).strip()

        # Prezzo fallback da JSON-LD
        if result["price"] is None:
            for ld in extract_jsonld(html):
                if isinstance(ld, dict):
                    offers = ld.get("offers", ld.get("Offers", {}))
                    if isinstance(offers, dict):
                        low = offers.get("lowPrice") or offers.get("price")
                        if low:
                            result["price"] = parse_price_eu(str(low))
                            break

        # Prezzo fallback da HTML buybox
        if result["price"] is None:
            for pattern in [
                r'class="a-price-whole">(\d[\d.,]*)</span>',
                r'id="priceblock_ourprice"[^>]*>\s*(?:€|EUR)?\s*([\d.,]+)',
                r'id="priceblock_dealprice"[^>]*>\s*(?:€|EUR)?\s*([\d.,]+)',
                r'class="a-offscreen">\s*(?:€|EUR)?\s*([\d.,]+)',
                r'"price"\s*:\s*"?([\d.,]+)"?\s*,\s*"priceCurrency"',
            ]:
                pm = re.search(pattern, html)
                if pm:
                    result["price"] = parse_price_eu(pm.group(1))
                    if result["price"]:
                        break

        # Disponibilita — sempre da HTML (twister isAvailable non e affidabile)
        if re.search(r'id="availability"[^>]*>.*?(?:Disponibilit|In stock|Auf Lager|En stock)', html, re.DOTALL | re.IGNORECASE):
            result["availability"] = "in_stock"
        elif re.search(r'(?:Non disponibile|Currently unavailable|Nicht verfügbar)', html, re.IGNORECASE):
            result["availability"] = "unavailable"

        # Venditore
        sm = re.search(r'id="sellerProfileTriggerId"[^>]*>(.*?)<', html)
        if sm:
            result["seller"] = sm.group(1).strip()
        elif re.search(r'(?:Venduto e spedito da|Ships from and sold by)\s*Amazon', html, re.IGNORECASE):
            result["seller"] = "Amazon"

    return result


def scrape_product_all_eu(asin: str, countries: list[str] | None = None) -> list[dict]:
    """Scrapa lo stesso ASIN su tutti gli Amazon EU."""
    targets = countries or ["it", "de", "fr", "es"]
    results = []
    for country in targets:
        domain = DOMAINS.get(country)
        if not domain:
            continue
        url = product_url(asin, domain)
        r = scrape_product(url)
        r["country"] = country
        r["domain"] = domain
        results.append(r)
    return results


def search_products(query: str, domain: str = "www.amazon.it", max_results: int = 5) -> list[dict]:
    """Cerca prodotti su Amazon e ritorna i primi risultati con prezzo."""
    search_url = f"https://{domain}/s?k={urllib.parse.quote(query)}"
    html = fetch(search_url)
    if not html:
        return []

    results = []
    # Pattern per risultati di ricerca Amazon
    for m in re.finditer(
        r'data-asin="([A-Z0-9]{10})".*?'
        r'class="a-size-(?:medium|base-plus)[^"]*"[^>]*>\s*'
        r'(?:<a[^>]*>)?\s*(.*?)\s*(?:</a>)?\s*</(?:span|h2)>',
        html, re.DOTALL
    ):
        asin = m.group(1)
        title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if not title or not asin:
            continue

        # Cerca prezzo vicino a questo risultato
        chunk_start = m.end()
        chunk = html[chunk_start:chunk_start + 2000]
        price = None
        pm = re.search(r'class="a-offscreen">\s*(?:€|EUR)\s*([\d.,]+)', chunk)
        if pm:
            price = parse_price_eu(pm.group(1))

        results.append({
            "asin": asin,
            "title": title,
            "price": price,
            "url": product_url(asin, domain),
            "site": "amazon",
            "domain": domain,
        })
        if len(results) >= max_results:
            break

    return results
