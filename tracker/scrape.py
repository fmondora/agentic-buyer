#!/usr/bin/env python3
"""CLI unificata per scraping prezzi — usata dagli agenti Claude via Bash.

Uso:
    python3.12 tracker/scrape.py product <url>
        Scrapa una pagina prodotto (auto-detect sito) → JSON

    python3.12 tracker/scrape.py amazon <url_or_asin>
        Scrapa prodotto Amazon → JSON

    python3.12 tracker/scrape.py amazon-eu <asin> [it,de,fr,es]
        Scrapa stesso ASIN su più Amazon EU → JSON

    python3.12 tracker/scrape.py idealo <url>
        Scrapa prodotto idealo → JSON

    python3.12 tracker/scrape.py trovaprezzi <url>
        Scrapa prodotto trovaprezzi → JSON

    python3.12 tracker/scrape.py search <query> [sito]
        Cerca un prodotto (sito: amazon|idealo|trovaprezzi|all) → JSON

Output: JSON su stdout, errori su stderr.
"""

import json
import sys
from pathlib import Path

# Aggiungi parent al path per import relativi
sys.path.insert(0, str(Path(__file__).parent.parent))

from tracker.scrapers import amazon, idealo, trovaprezzi, unieuro, mediaworld
from tracker.scrapers.base import result_json

SCRAPERS = {
    "amazon": amazon,
    "idealo": idealo,
    "trovaprezzi": trovaprezzi,
    "unieuro": unieuro,
    "mediaworld": mediaworld,
}


def detect_site(url: str) -> str:
    if "amazon" in url:
        return "amazon"
    if "idealo" in url:
        return "idealo"
    if "trovaprezzi" in url:
        return "trovaprezzi"
    if "unieuro" in url:
        return "unieuro"
    if "mediaworld" in url:
        return "mediaworld"
    return "unknown"


def cmd_product(args: list[str]):
    """Scrapa una URL prodotto (auto-detect sito)."""
    if not args:
        print("Uso: scrape.py product <url>", file=sys.stderr)
        sys.exit(1)
    url = args[0]
    site = detect_site(url)
    scraper = SCRAPERS.get(site)
    if not scraper:
        print(f"Sito non riconosciuto: {url}", file=sys.stderr)
        sys.exit(1)
    print(result_json([scraper.scrape_product(url)]))


def cmd_amazon(args: list[str]):
    """Scrapa un prodotto Amazon."""
    if not args:
        print("Uso: scrape.py amazon <url_or_asin>", file=sys.stderr)
        sys.exit(1)
    target = args[0]
    if target.startswith("http"):
        result = amazon.scrape_product(target)
    else:
        # È un ASIN
        result = amazon.scrape_product(amazon.product_url(target))
    print(result_json([result]))


def cmd_amazon_eu(args: list[str]):
    """Scrapa lo stesso ASIN su più Amazon EU."""
    if not args:
        print("Uso: scrape.py amazon-eu <asin> [it,de,fr,es]", file=sys.stderr)
        sys.exit(1)
    asin = args[0]
    countries = args[1].split(",") if len(args) > 1 else ["it", "de", "fr", "es"]
    results = amazon.scrape_product_all_eu(asin, countries)
    print(result_json(results))


def cmd_idealo(args: list[str]):
    """Scrapa un prodotto idealo."""
    if not args:
        print("Uso: scrape.py idealo <url>", file=sys.stderr)
        sys.exit(1)
    result = idealo.scrape_product(args[0])
    print(result_json([result]))


def cmd_trovaprezzi(args: list[str]):
    """Scrapa un prodotto trovaprezzi."""
    if not args:
        print("Uso: scrape.py trovaprezzi <url>", file=sys.stderr)
        sys.exit(1)
    result = trovaprezzi.scrape_product(args[0])
    print(result_json([result]))


def cmd_unieuro(args: list[str]):
    """Scrapa un prodotto unieuro.it."""
    if not args:
        print("Uso: scrape.py unieuro <url>", file=sys.stderr)
        sys.exit(1)
    result = unieuro.scrape_product(args[0])
    print(result_json([result]))


def cmd_mediaworld(args: list[str]):
    """Scrapa un prodotto mediaworld.it."""
    if not args:
        print("Uso: scrape.py mediaworld <url>", file=sys.stderr)
        sys.exit(1)
    result = mediaworld.scrape_product(args[0])
    print(result_json([result]))


def cmd_search(args: list[str]):
    """Cerca un prodotto su uno o più siti."""
    if not args:
        print("Uso: scrape.py search <query> [amazon|idealo|trovaprezzi|all]", file=sys.stderr)
        sys.exit(1)
    query = args[0]
    site = args[1] if len(args) > 1 else "all"

    results = []
    if site in ("amazon", "all"):
        results.extend(amazon.search_products(query))
    if site in ("idealo", "all"):
        results.extend(idealo.search_product(query))
    if site in ("trovaprezzi", "all"):
        results.extend(trovaprezzi.search_product(query))

    print(result_json(results))


def cmd_compare(args: list[str]):
    """Scrapa più URL in parallelo e confronta prezzi."""
    if not args:
        print("Uso: scrape.py compare <url1> <url2> [url3...]", file=sys.stderr)
        sys.exit(1)
    results = []
    for url in args:
        site = detect_site(url)
        scraper = SCRAPERS.get(site)
        if scraper:
            results.append(scraper.scrape_product(url))
        else:
            results.append({"url": url, "error": "sito_non_supportato"})
    print(result_json(results))


COMMANDS = {
    "product": cmd_product,
    "amazon": cmd_amazon,
    "amazon-eu": cmd_amazon_eu,
    "idealo": cmd_idealo,
    "trovaprezzi": cmd_trovaprezzi,
    "unieuro": cmd_unieuro,
    "mediaworld": cmd_mediaworld,
    "search": cmd_search,
    "compare": cmd_compare,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Buyer Scraper CLI")
        print(f"Uso: {sys.argv[0]} <comando> [args]")
        print(f"Comandi: {', '.join(COMMANDS.keys())}")
        print()
        print("Esempi:")
        print(f"  {sys.argv[0]} product https://www.amazon.it/dp/B0F44BHS8M")
        print(f"  {sys.argv[0]} amazon-eu B0F44BHS8M it,de,fr")
        print(f"  {sys.argv[0]} search 'LG OLED B5 55' idealo")
        print(f"  {sys.argv[0]} compare https://url1 https://url2")
        sys.exit(1)

    COMMANDS[sys.argv[1]](sys.argv[2:])
