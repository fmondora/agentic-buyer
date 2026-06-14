"""Scraper per Amazon EU — estrae prezzi da pagine prodotto e ricerca."""

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


def scrape_product(url: str) -> dict:
    """Scrapa una singola pagina prodotto Amazon."""
    html = fetch(url)
    if not html:
        return {"url": url, "price": None, "error": "fetch_failed"}

    result = {
        "url": url,
        "site": "amazon",
        "price": None,
        "title": None,
        "availability": None,
        "seller": None,
        "asin": extract_asin(url),
    }

    # Titolo
    m = re.search(r'id="productTitle"[^>]*>\s*(.*?)\s*<', html, re.DOTALL)
    if m:
        result["title"] = m.group(1).strip()

    # JSON-LD
    for ld in extract_jsonld(html):
        if isinstance(ld, dict):
            offers = ld.get("offers", ld.get("Offers", {}))
            if isinstance(offers, dict):
                low = offers.get("lowPrice") or offers.get("price")
                if low:
                    result["price"] = parse_price_eu(str(low))
                    break
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
                    break

    # Fallback: prezzo dal buybox
    if result["price"] is None:
        # Pattern "priceblock" / "a]priceToPay"
        for pattern in [
            r'class="a-price-whole">(\d[\d.,]*)</span>',
            r'id="priceblock_ourprice"[^>]*>\s*(?:€|EUR)?\s*([\d.,]+)',
            r'id="priceblock_dealprice"[^>]*>\s*(?:€|EUR)?\s*([\d.,]+)',
            r'class="a-offscreen">\s*(?:€|EUR)?\s*([\d.,]+)',
            r'"price"\s*:\s*"?([\d.,]+)"?\s*,\s*"priceCurrency"',
        ]:
            m = re.search(pattern, html)
            if m:
                result["price"] = parse_price_eu(m.group(1))
                if result["price"]:
                    break

    # Disponibilità
    if re.search(r'id="availability"[^>]*>.*?(?:Disponibilit|In stock|Auf Lager|En stock)', html, re.DOTALL | re.IGNORECASE):
        result["availability"] = "in_stock"
    elif re.search(r'(?:Non disponibile|Currently unavailable|Nicht verfügbar)', html, re.IGNORECASE):
        result["availability"] = "unavailable"

    # Venditore
    m = re.search(r'id="sellerProfileTriggerId"[^>]*>(.*?)<', html)
    if m:
        result["seller"] = m.group(1).strip()
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
