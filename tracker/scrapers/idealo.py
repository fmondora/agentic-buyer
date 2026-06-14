"""Scraper per idealo.it — usa le API frontend JSON per prezzi e storico."""

import json
import re
import urllib.parse
from .base import fetch, extract_jsonld, parse_price_eu, find_prices_in_text

DOMAINS = {
    "it": "www.idealo.it",
    "de": "www.idealo.de",
    "fr": "www.idealo.fr",
    "es": "www.idealo.es",
    "at": "www.idealo.at",
}

# Mappa country → siteId per l'API price-chart
SITE_IDS = {"it": 10, "de": 1, "fr": 7, "es": 9, "at": 3}


def extract_product_id(url: str) -> str | None:
    """Estrae l'ID prodotto numerico da un URL idealo."""
    m = re.search(r'/(\d{6,12})[-/]', url)
    return m.group(1) if m else None


def _api_headers(referer: str) -> dict:
    """Header per le API frontend idealo — simula Chrome reale."""
    return {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/148.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
        "Accept-Encoding": "identity",
        "Referer": referer,
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", '
                     '"Not/A)Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
    }


def fetch_price_history(product_id: str, country: str = "it",
                        period: str = "3M") -> dict | None:
    """Chiama l'API price-chart per lo storico prezzi.

    Ritorna dict con: startDate, data (lista punti), statistics.
    I prezzi sono in centesimi (2390 = 23.90€).
    """
    site_id = SITE_IDS.get(country, 10)
    domain = DOMAINS.get(country, DOMAINS["it"])
    url = (f"https://{domain}/price-chart/sites/{site_id}"
           f"/products/{product_id}/history?period={period}")
    referer = f"https://{domain}/confronta-prezzi/{product_id}/product.html"
    raw = fetch(url, headers=_api_headers(referer))
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def fetch_international_prices(product_id: str,
                               country: str = "it") -> list[dict]:
    """Chiama l'API internationalprices per confronto prezzi EU.

    Ritorna lista di {country, domain, price}.
    """
    domain = DOMAINS.get(country, DOMAINS["it"])
    url = (f"https://{domain}/offerpage/fragment/internationalprices"
           f"/products/{product_id}")
    referer = f"https://{domain}/confronta-prezzi/{product_id}/product.html"
    html = fetch(url, headers=_api_headers(referer))
    if not html:
        return []

    results = []
    for m in re.finditer(
        r"international_element_price=>([\d.]+);\s*"
        r"international_element_domain=>(\w+)",
        html,
    ):
        price = float(m.group(1))
        ctry = m.group(2)
        results.append({"country": ctry, "price": price,
                         "domain": f"idealo.{ctry}"})
    return results


def scrape_product(url: str) -> dict:
    """Scrapa una pagina prodotto idealo con API + HTML fallback."""
    product_id = extract_product_id(url)
    country = "it"
    for code, domain in DOMAINS.items():
        if domain in url:
            country = code
            break

    result = {
        "url": url,
        "site": "idealo",
        "price": None,
        "title": None,
        "offers": [],
        "offer_count": 0,
        "product_id": product_id,
        "price_history": None,
        "international_prices": [],
    }

    # 1) API price-chart — la fonte più affidabile per il prezzo corrente
    if product_id:
        history = fetch_price_history(product_id, country, period="1W")
        if history and history.get("data"):
            last_point = history["data"][-1]
            result["price"] = last_point["y"] / 100.0
            stats = history.get("statistics", {})
            result["price_history"] = {
                "lowest": stats.get("lowestPrice", 0) / 100.0,
                "highest": stats.get("highestPrice", 0) / 100.0,
                "average": stats.get("avgPrice", 0) / 100.0,
            }

        # Prezzi internazionali
        intl = fetch_international_prices(product_id, country)
        if intl:
            result["international_prices"] = intl

    # 2) HTML fallback — per titolo, offerte, e prezzo se API fallisce
    html = fetch(url)
    if html:
        # Titolo
        m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.DOTALL)
        if m:
            result["title"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

        # JSON-LD per titolo e prezzo fallback
        for ld in extract_jsonld(html):
            if not isinstance(ld, dict):
                continue
            if ld.get("name"):
                result["title"] = ld["name"]
            offers = ld.get("offers", {})
            if isinstance(offers, dict):
                if result["price"] is None:
                    low = offers.get("lowPrice")
                    if low:
                        result["price"] = parse_price_eu(str(low))
                count = offers.get("offerCount")
                if count:
                    result["offer_count"] = int(count)

        # Fallback HTML per prezzo
        if result["price"] is None:
            m = re.search(r'"lowPrice"\s*:\s*"?([\d.,]+)"?', html)
            if m:
                result["price"] = parse_price_eu(m.group(1))

    return result


def search_product(query: str, country: str = "it") -> list[dict]:
    """Cerca un prodotto su idealo e ritorna i risultati."""
    domain = DOMAINS.get(country, DOMAINS["it"])
    search_url = f"https://{domain}/trova/{urllib.parse.quote(query)}.html"
    html = fetch(search_url)
    if not html:
        return []

    results = []
    for m in re.finditer(
        r'<a[^>]*href="(https://[^"]*confronta-prezzi[^"]*)"[^>]*>.*?'
        r'class="[^"]*productName[^"]*"[^>]*>\s*(.*?)\s*<.*?'
        r'([\d.,]+)\s*(?:€|&euro;)',
        html, re.DOTALL
    ):
        url = m.group(1)
        title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        price = parse_price_eu(m.group(3))
        if title and price:
            results.append({
                "url": url,
                "title": title,
                "price": price,
                "site": "idealo",
                "country": country,
            })
            if len(results) >= 5:
                break

    return results
