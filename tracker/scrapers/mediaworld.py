"""Scraper per mediaworld.it — estrae prezzi da pagine prodotto."""

import re
import urllib.parse
from .base import fetch, extract_jsonld, parse_price_eu, find_prices_in_text

HEADERS_MW = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "identity",
}


def scrape_product(url: str) -> dict:
    """Scrapa una pagina prodotto mediaworld.it."""
    html = fetch(url, headers=HEADERS_MW)
    if not html:
        return {"url": url, "site": "mediaworld", "price": None, "error": "fetch_failed"}

    result = {
        "url": url,
        "site": "mediaworld",
        "price": None,
        "title": None,
        "availability": None,
        "pickup_available": None,
    }

    # Titolo
    m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.DOTALL)
    if m:
        result["title"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    # JSON-LD
    for ld in extract_jsonld(html):
        if not isinstance(ld, dict):
            continue
        if ld.get("@type") == "Product" or "offers" in ld:
            if ld.get("name"):
                result["title"] = ld["name"]
            offers = ld.get("offers", {})
            if isinstance(offers, dict):
                price = offers.get("price") or offers.get("lowPrice")
                if price:
                    result["price"] = parse_price_eu(str(price))
                avail = offers.get("availability", "")
                if "InStock" in avail:
                    result["availability"] = "in_stock"
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

    # Fallback: pattern prezzo
    if result["price"] is None:
        for pattern in [
            r'data-price="([\d.,]+)"',
            r'class="[^"]*price[^"]*"[^>]*>\s*([\d.,]+)\s*(?:€|&euro;)',
            r'<meta[^>]*property="product:price:amount"[^>]*content="([\d.,]+)"',
        ]:
            m = re.search(pattern, html)
            if m:
                result["price"] = parse_price_eu(m.group(1))
                if result["price"]:
                    break

    # Ritiro in negozio
    if re.search(r'(?:ritiro.*negozio|pick.?up|disponibile.*negozio)', html, re.IGNORECASE):
        result["pickup_available"] = True

    # Ultimo fallback
    if result["price"] is None:
        prices = find_prices_in_text(html, min_price=100)
        if prices:
            result["price"] = min(prices)

    return result
