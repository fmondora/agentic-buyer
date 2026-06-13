#!/usr/bin/env python3
"""Price checker per Buyer — scrapa prezzi da idealo.it e trovaprezzi.it."""

import csv
import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, date
from pathlib import Path

TRACKER_DIR = Path(__file__).parent
WATCHLIST = TRACKER_DIR / "watchlist.json"
HISTORY_DIR = TRACKER_DIR / "history"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml",
}


def fetch_page(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} per {url}", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"  Errore fetch {url}: {e}", file=sys.stderr)
        return ""


def extract_price_idealo(html: str) -> float | None:
    """Estrae il prezzo minimo da idealo.it via JSON-LD o pattern HTML."""
    # JSON-LD structured data
    match = re.search(r'"lowPrice"\s*:\s*"?([\d.,]+)"?', html)
    if match:
        price_str = match.group(1).replace(".", "").replace(",", ".")
        try:
            return float(price_str)
        except ValueError:
            pass

    # Fallback: pattern prezzo nel HTML
    match = re.search(r'class="[^"]*price[^"]*"[^>]*>[\s]*(\d[\d.,]*)\s*[€&euro;]', html)
    if match:
        price_str = match.group(1).replace(".", "").replace(",", ".")
        try:
            return float(price_str)
        except ValueError:
            pass

    # Fallback: qualsiasi prezzo in euro nel testo
    prices = re.findall(r'(\d{2,4})[.,](\d{2})\s*(?:€|&euro;|EUR)', html)
    if prices:
        values = []
        for integer, decimal in prices:
            integer_clean = integer.replace(".", "")
            try:
                values.append(float(f"{integer_clean}.{decimal}"))
            except ValueError:
                continue
        if values:
            return min(v for v in values if v > 50)

    return None


def extract_price_trovaprezzi(html: str) -> float | None:
    """Estrae il prezzo minimo da trovaprezzi.it."""
    # Pattern specifico trovaprezzi: "a partire da XX,XX €"
    match = re.search(r'a partire da\s*(\d[\d.,]*)\s*€', html)
    if match:
        price_str = match.group(1).replace(".", "").replace(",", ".")
        try:
            return float(price_str)
        except ValueError:
            pass

    # JSON-LD
    match = re.search(r'"lowPrice"\s*:\s*"?([\d.,]+)"?', html)
    if match:
        price_str = match.group(1).replace(".", "").replace(",", ".")
        try:
            return float(price_str)
        except ValueError:
            pass

    return None


def check_product(product: dict) -> list[dict]:
    """Controlla i prezzi per un prodotto su tutte le sue fonti."""
    results = []
    for source in product["sources"]:
        html = fetch_page(source["url"])
        if not html:
            results.append({"site": source["site"], "price": None, "url": source["url"]})
            continue

        if source["site"] == "idealo":
            price = extract_price_idealo(html)
        elif source["site"] == "trovaprezzi":
            price = extract_price_trovaprezzi(html)
        else:
            price = extract_price_idealo(html)  # fallback generico

        results.append({"site": source["site"], "price": price, "url": source["url"]})

    return results


def save_prices(product_id: str, results: list[dict]):
    """Salva i prezzi nel CSV storico."""
    csv_path = HISTORY_DIR / f"{product_id}.csv"
    is_new = not csv_path.exists()

    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["date", "site", "price", "url"])
        today = date.today().isoformat()
        for r in results:
            if r["price"] is not None:
                writer.writerow([today, r["site"], f"{r['price']:.2f}", r["url"]])


def load_history(product_id: str) -> list[dict]:
    """Carica lo storico prezzi da CSV."""
    csv_path = HISTORY_DIR / f"{product_id}.csv"
    if not csv_path.exists():
        return []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        return list(reader)


def print_report(product: dict, results: list[dict], history: list[dict]):
    """Stampa report per un prodotto."""
    print(f"\n{'='*60}")
    print(f"  {product['name']}")
    print(f"  Budget: {product['budget']}€ | Alert sotto: {product.get('alert_below', 'N/A')}€")
    print(f"{'='*60}")

    # Prezzi odierni
    print(f"\n  Prezzi oggi ({date.today().isoformat()}):")
    min_price = None
    for r in results:
        if r["price"] is not None:
            marker = ""
            if min_price is None or r["price"] < min_price:
                min_price = r["price"]
            if product.get("alert_below") and r["price"] <= product["alert_below"]:
                marker = " << SOTTO SOGLIA ALERT!"
            print(f"    {r['site']:>15}: {r['price']:>8.2f}€{marker}")
        else:
            print(f"    {r['site']:>15}: non disponibile")

    if min_price:
        delta_budget = product["budget"] - min_price
        print(f"\n  Prezzo minimo: {min_price:.2f}€ (risparmi {delta_budget:.0f}€ sul budget)")

    # Storico
    if history:
        prices_by_date = {}
        for h in history:
            d = h["date"]
            p = float(h["price"])
            if d not in prices_by_date or p < prices_by_date[d]:
                prices_by_date[d] = p

        if len(prices_by_date) > 1:
            dates = sorted(prices_by_date.keys())
            print(f"\n  Andamento ({len(dates)} rilevazioni):")
            first_price = prices_by_date[dates[0]]
            for d in dates[-10:]:  # ultime 10
                p = prices_by_date[d]
                delta = p - first_price
                bar_len = max(0, min(40, int((p - 300) / 20)))
                bar = "█" * bar_len
                sign = "+" if delta > 0 else ""
                print(f"    {d}  {p:>8.2f}€  {bar}  ({sign}{delta:.0f}€)")

            # Stats
            all_prices = list(prices_by_date.values())
            print(f"\n  Min storico: {min(all_prices):.2f}€ | Max: {max(all_prices):.2f}€ | Media: {sum(all_prices)/len(all_prices):.2f}€")
    else:
        print("\n  Nessuno storico precedente — prima rilevazione.")


def cmd_check(args):
    """Controlla prezzi per tutti i prodotti in watchlist."""
    products = json.loads(WATCHLIST.read_text())
    for product in products:
        if args and product["id"] not in args:
            continue
        print(f"Controllo {product['name']}...")
        results = check_product(product)
        save_prices(product["id"], results)
        history = load_history(product["id"])
        print_report(product, results, history)


def cmd_list(args):
    """Lista prodotti tracciati."""
    products = json.loads(WATCHLIST.read_text())
    print(f"\nProdotti tracciati: {len(products)}\n")
    for p in products:
        history = load_history(p["id"])
        last_price = "N/A"
        if history:
            last_price = f"{float(history[-1]['price']):.0f}€"
        print(f"  {p['id']:30s}  {last_price:>8s}  alert<{p.get('alert_below', 'N/A')}€  {p['name']}")


def cmd_add(args):
    """Aggiunge un prodotto alla watchlist. Uso: add <id> <name> <idealo_url> [budget] [alert]"""
    if len(args) < 3:
        print("Uso: check_prices.py add <id> <name> <idealo_url> [budget] [alert_below]")
        sys.exit(1)

    product_id, name, url = args[0], args[1], args[2]
    budget = int(args[3]) if len(args) > 3 else 1000
    alert = int(args[4]) if len(args) > 4 else budget - 100

    products = json.loads(WATCHLIST.read_text())

    if any(p["id"] == product_id for p in products):
        print(f"Prodotto {product_id} già presente.")
        sys.exit(1)

    site = "idealo" if "idealo" in url else "trovaprezzi" if "trovaprezzi" in url else "altro"

    products.append({
        "id": product_id,
        "name": name,
        "sources": [{"site": site, "url": url}],
        "budget": budget,
        "alert_below": alert,
        "added": date.today().isoformat(),
    })

    WATCHLIST.write_text(json.dumps(products, indent=2, ensure_ascii=False) + "\n")
    print(f"Aggiunto: {name} (alert sotto {alert}€)")


def cmd_history(args):
    """Mostra storico completo per un prodotto."""
    if not args:
        print("Uso: check_prices.py history <product_id>")
        sys.exit(1)
    history = load_history(args[0])
    if not history:
        print("Nessuno storico.")
        return
    print(f"\n{'Data':<12} {'Sito':<15} {'Prezzo':>10}")
    print("-" * 40)
    for h in history:
        print(f"{h['date']:<12} {h['site']:<15} {float(h['price']):>9.2f}€")


if __name__ == "__main__":
    HISTORY_DIR.mkdir(exist_ok=True)

    commands = {
        "check": cmd_check,
        "list": cmd_list,
        "add": cmd_add,
        "history": cmd_history,
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Buyer Price Tracker")
        print(f"Uso: {sys.argv[0]} <comando> [args]")
        print(f"Comandi: {', '.join(commands.keys())}")
        sys.exit(1)

    commands[sys.argv[1]](sys.argv[2:])
