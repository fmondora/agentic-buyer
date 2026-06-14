"""Scraper per CamelCamelCamel — storico prezzi Amazon da tabella HTML."""

import re
from .base import fetch, parse_price_eu


# Mappa country code → dominio CamelCamelCamel
LOCALES = {
    "it": "it", "de": "de", "fr": "fr", "es": "es",
    "uk": "uk", "us": "us", "ca": "ca",
}

CHART_BASE = "https://charts.camelcamelcamel.com"


def _ccc_headers(locale: str = "it") -> dict:
    return {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/148.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,*/*",
        "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
        "Accept-Encoding": "identity",
    }


def chart_url(asin: str, locale: str = "it",
              chart_type: str = "new", period: str = "all") -> str:
    """Genera URL del grafico prezzi CamelCamelCamel.

    chart_type: 'amazon', 'new', 'used', 'amazon-new', 'amazon-new-used'
    period: '1m', '3m', '6m', '1y', 'all'
    """
    return (f"{CHART_BASE}/{locale}/{asin}/{chart_type}.png"
            f"?force=1&zero=0&w=855&h=513&desired=false"
            f"&legend=1&ilt=1&tp={period}&fo=0&lang=it_IT")


def scrape_product(asin: str, locale: str = "it") -> dict:
    """Scrapa la pagina CamelCamelCamel per un ASIN e estrae i dati prezzi."""
    url = f"https://{locale}.camelcamelcamel.com/product/{asin}"
    html = fetch(url, headers=_ccc_headers(locale), timeout=20)

    result = {
        "asin": asin,
        "locale": locale,
        "site": "camelcamelcamel",
        "url": url,
        "title": None,
        "prices": {
            "amazon": {"lowest": None, "highest": None, "current": None, "average": None},
            "third_party_new": {"lowest": None, "highest": None, "current": None, "average": None},
            "third_party_used": {"lowest": None, "highest": None, "current": None, "average": None},
        },
        "product_info": {},
        "chart_urls": {
            "new": chart_url(asin, locale, "new"),
            "amazon": chart_url(asin, locale, "amazon"),
            "used": chart_url(asin, locale, "used"),
        },
        "last_update": None,
    }

    if not html:
        result["error"] = "fetch_failed"
        return result

    # Titolo
    m = re.search(r'<title>(.*?)(?:\s*\|)', html)
    if m:
        result["title"] = m.group(1).strip()

    # Tabella prezzi: "Price Type | Lowest Ever | Highest Ever | Current | Average"
    price_rows = {
        "amazon": r"Amazon",
        "third_party_new": r"3rd Party New",
        "third_party_used": r"3rd Party Used",
    }
    for key, label in price_rows.items():
        pattern = (
            rf'<tr[^>]*>.*?{label}.*?'
            rf'<td[^>]*>(.*?)</td>.*?'  # lowest
            rf'<td[^>]*>(.*?)</td>.*?'  # highest
            rf'<td[^>]*>(.*?)</td>.*?'  # current
            rf'<td[^>]*>(.*?)</td>'     # average
        )
        m = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if m:
            for i, field in enumerate(["lowest", "highest", "current", "average"]):
                raw = re.sub(r'<[^>]+>', '', m.group(i + 1)).strip()
                raw = raw.split('\n')[0].strip()
                if raw and raw != "-":
                    price = parse_price_eu(raw)
                    if price:
                        result["prices"][key][field] = price

    # Info prodotto: tabella chiave-valore
    for m in re.finditer(
        r'<td[^>]*>\s*(Product group|Category|Manufacturer|Model|'
        r'List price|EAN|SKU|Last update scan)\s*</td>\s*'
        r'<td[^>]*>(.*?)</td>',
        html, re.DOTALL | re.IGNORECASE
    ):
        key = m.group(1).strip().lower().replace(" ", "_")
        val = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if val and val != "-":
            result["product_info"][key] = val

    # Last update
    m = re.search(r'Last update scan.*?on\s+(\w+ \d+,\s*\d{4})', html, re.DOTALL)
    if m:
        result["last_update"] = m.group(1).strip()

    return result
