"""Utilità comuni per gli scrapers — fetch HTTP e parsing prezzi."""

import json
import re
import urllib.request
import urllib.error
import sys
from typing import Any


HEADERS_DESKTOP = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "identity",
}


def fetch(url: str, headers: dict | None = None, timeout: int = 15) -> str:
    """Fetch una pagina web, ritorna HTML come stringa. Stringa vuota se errore."""
    hdrs = headers or HEADERS_DESKTOP
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} per {url}", file=sys.stderr)
        return ""
    except Exception as e:
        print(f"Errore fetch {url}: {e}", file=sys.stderr)
        return ""


def extract_jsonld(html: str) -> list[dict]:
    """Estrae tutti i blocchi JSON-LD da una pagina HTML."""
    results = []
    for match in re.finditer(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL):
        try:
            data = json.loads(match.group(1))
            if isinstance(data, list):
                results.extend(data)
            else:
                results.append(data)
        except json.JSONDecodeError:
            continue
    return results


def parse_price_eu(price_str: str) -> float | None:
    """Parsa un prezzo in formato europeo (1.234,56) o internazionale (1234.56)."""
    s = price_str.strip().replace("€", "").replace("EUR", "").replace("\xa0", "").strip()
    if not s:
        return None
    # Formato EU: 1.234,56
    if "," in s and ("." not in s or s.rindex(",") > s.rindex(".")):
        s = s.replace(".", "").replace(",", ".")
    # Formato US: 1,234.56
    elif "," in s:
        s = s.replace(",", "")
    try:
        val = float(s)
        return val if val > 0 else None
    except ValueError:
        return None


def find_prices_in_text(html: str, min_price: float = 50, max_price: float = 50000) -> list[float]:
    """Trova tutti i prezzi in euro nel testo HTML."""
    prices = []
    for m in re.finditer(r'(\d[\d.,]*)\s*(?:€|&euro;|EUR)', html):
        p = parse_price_eu(m.group(1))
        if p and min_price <= p <= max_price:
            prices.append(p)
    return prices


def result_json(results: list[dict]) -> str:
    """Serializza risultati in JSON per stdout."""
    return json.dumps(results, indent=2, ensure_ascii=False)
