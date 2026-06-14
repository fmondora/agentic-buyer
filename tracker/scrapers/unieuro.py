"""Scraper per unieuro.it — estrae prezzi da pagine prodotto."""

import re
import urllib.parse
from .base import fetch, extract_jsonld, parse_price_eu, find_prices_in_text

HEADERS_UNIEURO = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "identity",
    "Referer": "https://www.unieuro.it/",
}


def scrape_product(url: str) -> dict:
    """Scrapa una pagina prodotto unieuro.it."""
    html = fetch(url, headers=HEADERS_UNIEURO)
    if not html:
        return {"url": url, "site": "unieuro", "price": None, "error": "fetch_failed"}

    result = {
        "url": url,
        "site": "unieuro",
        "price": None,
        "title": None,
        "availability": None,
        "pickup_available": None,
    }

    # Titolo
    m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.DOTALL)
    if m:
        result["title"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    # JSON-LD — fonte più affidabile
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
                elif "OutOfStock" in avail:
                    result["availability"] = "out_of_stock"
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

    # Fallback: data-price attribute
    if result["price"] is None:
        m = re.search(r'data-price="([\d.,]+)"', html)
        if m:
            result["price"] = parse_price_eu(m.group(1))

    # Fallback: current-price class
    if result["price"] is None:
        m = re.search(r'class="[^"]*current-price[^"]*"[^>]*>\s*([\d.,]+)\s*(?:€|&euro;)', html)
        if m:
            result["price"] = parse_price_eu(m.group(1))

    # Fallback: meta tag
    if result["price"] is None:
        m = re.search(r'<meta[^>]*property="product:price:amount"[^>]*content="([\d.,]+)"', html)
        if m:
            result["price"] = parse_price_eu(m.group(1))

    # Clicca e Ritira disponibile?
    if re.search(r'(?:clicca.*ritira|ritiro.*negozio|pick.?up)', html, re.IGNORECASE):
        result["pickup_available"] = True

    # Ultimo fallback: prezzi nel testo
    if result["price"] is None:
        prices = find_prices_in_text(html, min_price=100)
        if prices:
            result["price"] = min(prices)

    return result


def search_product(query: str) -> list[dict]:
    """Cerca un prodotto su unieuro.it."""
    search_url = f"https://www.unieuro.it/online/ricerca?q={urllib.parse.quote(query)}"
    html = fetch(search_url, headers=HEADERS_UNIEURO)
    if not html:
        return []

    results = []
    # JSON-LD nei risultati
    for ld in extract_jsonld(html):
        if isinstance(ld, dict) and ld.get("@type") == "Product":
            price = None
            offers = ld.get("offers", {})
            if isinstance(offers, dict):
                p = offers.get("price") or offers.get("lowPrice")
                if p:
                    price = parse_price_eu(str(p))
            results.append({
                "title": ld.get("name", ""),
                "price": price,
                "url": ld.get("url", ""),
                "site": "unieuro",
            })

    # Fallback: pattern HTML
    if not results:
        for m in re.finditer(
            r'<a[^>]*href="(/online/[^"]*pid[^"]*)"[^>]*>.*?'
            r'([\d.,]+)\s*(?:€|&euro;)',
            html, re.DOTALL
        ):
            url = f"https://www.unieuro.it{m.group(1)}"
            price = parse_price_eu(m.group(2))
            if price:
                results.append({"url": url, "price": price, "site": "unieuro"})
                if len(results) >= 5:
                    break

    return results
