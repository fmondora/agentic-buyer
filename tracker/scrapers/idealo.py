"""Scraper per idealo.it — estrae prezzo minimo e lista offerte."""

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


def scrape_product(url: str) -> dict:
    """Scrapa una pagina prodotto idealo e restituisce prezzo minimo + offerte."""
    html = fetch(url)
    if not html:
        return {"url": url, "site": "idealo", "price": None, "error": "fetch_failed"}

    result = {
        "url": url,
        "site": "idealo",
        "price": None,
        "title": None,
        "offers": [],
        "offer_count": 0,
    }

    # Titolo
    m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.DOTALL)
    if m:
        result["title"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    # JSON-LD — fonte più affidabile
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
        elif isinstance(offers, list):
            prices = []
            for o in offers:
                p = o.get("price") or o.get("lowPrice")
                if p:
                    parsed = parse_price_eu(str(p))
                    if parsed:
                        prices.append(parsed)
            if prices:
                result["price"] = min(prices)

    # Fallback: pattern HTML per "lowPrice"
    if result["price"] is None:
        m = re.search(r'"lowPrice"\s*:\s*"?([\d.,]+)"?', html)
        if m:
            result["price"] = parse_price_eu(m.group(1))

    # Fallback: pattern prezzo nel HTML
    if result["price"] is None:
        m = re.search(r'class="[^"]*price[^"]*"[^>]*>\s*([\d.,]+)\s*[€&]', html)
        if m:
            result["price"] = parse_price_eu(m.group(1))

    # Estrai lista offerte (venditori + prezzi)
    for om in re.finditer(
        r'class="[^"]*resultList[^"]*".*?'
        r'(?:class="[^"]*shopName[^"]*"[^>]*>\s*(.*?)\s*<).*?'
        r'([\d.,]+)\s*(?:€|&euro;)',
        html, re.DOTALL
    ):
        shop = re.sub(r'<[^>]+>', '', om.group(1)).strip()
        price = parse_price_eu(om.group(2))
        if shop and price:
            result["offers"].append({"shop": shop, "price": price})

    # Ultimo fallback: prezzi dal testo
    if result["price"] is None:
        prices = find_prices_in_text(html, min_price=50)
        if prices:
            result["price"] = min(prices)

    return result


def search_product(query: str, country: str = "it") -> list[dict]:
    """Cerca un prodotto su idealo e ritorna i risultati."""
    domain = DOMAINS.get(country, DOMAINS["it"])
    search_url = f"https://{domain}/trova/{urllib.parse.quote(query)}.html"
    html = fetch(search_url)
    if not html:
        return []

    results = []
    # Pattern per risultati di ricerca idealo
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
