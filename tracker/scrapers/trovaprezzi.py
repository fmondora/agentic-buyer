"""Scraper per trovaprezzi.it — estrae prezzo minimo e lista offerte."""

import re
import urllib.parse
from .base import fetch, extract_jsonld, parse_price_eu, find_prices_in_text


def scrape_product(url: str) -> dict:
    """Scrapa una pagina prodotto trovaprezzi.it."""
    html = fetch(url)
    if not html:
        return {"url": url, "site": "trovaprezzi", "price": None, "error": "fetch_failed"}

    result = {
        "url": url,
        "site": "trovaprezzi",
        "price": None,
        "title": None,
        "offers": [],
        "offer_count": 0,
    }

    # Titolo
    m = re.search(r'<h1[^>]*>\s*(.*?)\s*</h1>', html, re.DOTALL)
    if m:
        result["title"] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    # "a partire da XX,XX €" — pattern specifico trovaprezzi
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

    # Ultimo fallback
    if result["price"] is None:
        prices = find_prices_in_text(html, min_price=50)
        if prices:
            result["price"] = min(prices)

    return result


def search_product(query: str) -> list[dict]:
    """Cerca un prodotto su trovaprezzi.it."""
    search_url = f"https://www.trovaprezzi.it/prezzi_televisori-lcd-plasma.aspx?libera={urllib.parse.quote(query)}"
    html = fetch(search_url)
    if not html:
        return []

    results = []
    for m in re.finditer(
        r'<a[^>]*href="(https://www\.trovaprezzi\.it/[^"]*prezzi-scheda-prodotto[^"]*)"[^>]*>.*?'
        r'([\d.,]+)\s*(?:€|&euro;)',
        html, re.DOTALL
    ):
        url = m.group(1)
        price = parse_price_eu(m.group(2))
        # Estrai nome dal URL
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
