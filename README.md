# Buyer — Multi-Agent Smart Shopping System

A native Claude Code system that evaluates products through 9 specialized agents. Every purchase is scored across 8 dimensions: price, reviews, technical specs, real-world performance, sustainability, lifecycle, brand reputation, and purchase timing strategy.

## How it works

```
/buy bluetooth headphones budget 200€
```

The system runs a 4-stage pipeline:

1. **Discovery** (foreground) — asks 5-6 quick questions to understand what you really need, then personalizes search weights
2. **7 research agents** (parallel, background) — search the web via WebSearch + WebFetch + Python scrapers
3. **StrategicBuyer** (sequential, foreground) — receives the products found by the 7 agents and analyzes purchase timing: price trends, seasonality, manufacturer cycles, EU price comparison
4. **Synthesis** — cross-references all 8 agents, calculates weighted scores, saves structured JSON data and generates a comprehensive markdown report

The final report contains the full reasoning from all agents, not just the verdict. It serves as a reference to resume context in future sessions.

## Pipeline Architecture

```
User
  |
  v
Discovery (foreground, interactive)
  | enriched spec + custom weights
  v
7 agents (parallel, background)
  |-- PriceHunter       -> markdown + JSON (prices, ASIN, idealo_id)
  |-- ReviewAnalyst      -> markdown + JSON (ratings, sentiment)
  |-- SpecComparer       -> markdown + JSON (specs, energy class)
  |-- TechnicalCritic    -> markdown + JSON (real measurements)
  |-- SustainabilityScout -> markdown + JSON (certifications, emissions)
  |-- LifecycleAdvisor   -> markdown + JSON (repairability, lifecycle)
  '-- BrandRater         -> markdown + JSON (tier, ethics, safety gate)
  | unified product list + structured data
  v
StrategicBuyer (foreground, sequential)
  -> markdown + JSON (timing verdict, trends, seasonality)
  v
Synthesis -> tracker/results/{date}-{slug}/
             |-- spec.json           (discovery spec + weights)
             |-- agents/*.json       (structured output per agent)
             |-- products.json       (unified cross-agent product list)
             '-- scores.json         (calculated weighted scores)
  v
Report -> reports/{date}-{slug}.md
```

### Why sequential StrategicBuyer?

The StrategicBuyer makes a **final strategic assessment** on the products found by the other agents. It needs their results (product names, ASINs, idealo IDs, prices, brand info, product cycle stage) to run price history analysis on the right products. Running it in parallel would mean it has to search for products independently, duplicating work and potentially analyzing different products.

### Dual output: Markdown + JSON

Every agent produces two outputs:

1. **Markdown** — rich narrative analysis for human reading
2. **JSON appendice** — structured data (`json:structured-output` fenced block) for machine processing

This enables:
- Recalculating scores with different weights without re-running agents
- Comparing results across searches ("is the Samsung cheaper than last week?")
- Querying structured data ("show all products with brand score > 8")
- Graceful degradation: if an agent skips JSON, the orchestrator falls back to markdown

The JSON schema is defined in `.claude/agents/tools/output-schema.md`.

## Commands

| Command | What it does |
|---------|-------------|
| `/buy <product>` | Full research with 9 agents, generates report + structured data |
| `/buy-incognito <product>` | Same pipeline as `/buy` but writes nothing to disk |
| `/track add <product>` | Add a product to the price tracker |
| `/track check` | Check prices for all tracked products |
| `/track list` | Show the watchlist |
| `/track history <id>` | Price history for a product |
| `/track safety` | Check Safety Gate/RAPEX alerts for purchased products |

## Agents

### Discovery (foreground, step 1)
Interactive agent that asks numbered inline-choice questions. Produces an enriched spec and customizes weights based on answers (e.g., "durability matters" -> Lifecycle +10%, Price -10%).

### 7 Research Agents (parallel, background, step 2)

| Agent | What it searches | Default weight |
|-------|-----------------|---------------|
| **PriceHunter** | Prices on Amazon EU (9 countries), idealo, trovaprezzi, eBay, MediaWorld, Unieuro | 18% |
| **ReviewAnalyst** | Reviews on Amazon, YouTube, forums, Reddit, Altroconsumo, RTings | 13% |
| **SpecComparer** | Technical datasheets, EPREL energy labels, comparison tables | 13% |
| **TechnicalCritic** | Real-world calibrated performance, HDR measurements, Filmmaker Mode quality | 10% |
| **SustainabilityScout** | Certifications, CO2 scopes, biodiversity, CDP rating, greenwashing | 8% |
| **LifecycleAdvisor** | French repairability index, iFixit scores, spare parts, resale value | 8% |
| **BrandRater** | Reliability, Safety Gate/RAPEX alerts, ethics, local vs offshore production | 18% |

### StrategicBuyer (sequential, foreground, step 3)

| Agent | What it analyzes | Default weight |
|-------|-----------------|---------------|
| **StrategicBuyer** | Price trends (idealo history), seasonality (Prime Day, Black Friday...), manufacturer pricing cycles, EU price comparison, CamelCamelCamel history | 12% |

Produces one of 5 verdicts per product:

| Verdict | Meaning |
|---------|---------|
| **BUY NOW** | Price at/near minimum, no discount event coming, stockout risk |
| **BUY SOON** | Good price, might drop slightly. Act within 2 weeks |
| **WAIT FOR EVENT** | Discount event imminent (< 4 weeks). Specifies which one |
| **WAIT FOR DROP** | Downward trend, product cycle declining |
| **RISK** | Price above average, high volatility, significant drop possible |

Weights are customized by Discovery for each search.

## Scraper CLI

Python scrapers (stdlib only, zero dependencies) that extract structured price data via frontend APIs:

```bash
# Product page (auto-detect site)
python3.12 tracker/scrape.py product <url>

# Amazon: single product via twister API
python3.12 tracker/scrape.py amazon <url_or_asin>

# Amazon: same ASIN across EU countries
python3.12 tracker/scrape.py amazon-eu <asin> it,de,fr,es

# idealo: product + price history + international prices
python3.12 tracker/scrape.py idealo <url>
python3.12 tracker/scrape.py idealo-history <product_id> 3M
python3.12 tracker/scrape.py idealo-intl <product_id>

# trovaprezzi: product + price history
python3.12 tracker/scrape.py trovaprezzi <url>
python3.12 tracker/scrape.py trovaprezzi-history <slug>

# CamelCamelCamel: Amazon price history
python3.12 tracker/scrape.py camel <asin> [locale]

# Search across sites
python3.12 tracker/scrape.py search "query" [amazon|idealo|trovaprezzi|all]

# Compare multiple URLs
python3.12 tracker/scrape.py compare <url1> <url2> <url3>
```

### API Strategy

Each scraper uses frontend APIs as primary data source with HTML fallback:

| Site | Primary API | Fallback |
|------|------------|----------|
| **idealo** | `price-chart` JSON API (prices in cents) + `internationalprices` HTML fragment | HTML + JSON-LD |
| **Amazon** | Twister dimension slots API (streaming JSON) | HTML + JSON-LD |
| **trovaprezzi** | `price_chart` API (session + CSRF required) | HTML scraping |
| **CamelCamelCamel** | HTML tables (Cloudflare blocks urllib) | WebSearch + chart PNG URLs |
| **Unieuro/MediaWorld** | — | HTML + JSON-LD |

## Persistent Data

### Results (`tracker/results/`)
Each `/buy` search creates a directory with structured JSON:
```
tracker/results/2026-06-14-tv-55-pollici/
  spec.json           # Discovery spec + custom weights
  agents/
    price-hunter.json  # Structured output from each agent
    review-analyst.json
    ...
  products.json        # Unified product list (cross-agent merge)
  scores.json          # Calculated weighted scores
```

### Reports (`reports/`)
Comprehensive markdown reports with full agent reasoning. Self-contained — readable without conversation context.

### Learnings (`.claude/agents/learnings/`)
Each agent accumulates experience across sessions:
- Reliable and problematic data sources
- Effective search patterns per category
- Category-specific notes (e.g., "Samsung doesn't support Dolby Vision", "TCL throttles HDR in EU via firmware")

Read BEFORE each search, updated AFTER.

### Purchased Products (`tracker/purchased.json`)
Registry of completed purchases with brand, model, price paid, date. Used for Safety Gate monitoring and feedback tracking.

## Site Playbooks

Reusable navigation instructions in `.claude/agents/tools/`:

| Playbook | Purpose |
|----------|---------|
| `amazon-eu.md` | All 9 EU Amazon domains, ASIN-based cross-border search |
| `idealo.md` | EU price comparator, history API, international prices |
| `trovaprezzi.md` | Italian price comparator, session management |
| `ebay.md` | Auctions and buy-it-now, multi-country |
| `global-search.md` | Worldwide search with duty/VAT calculation toward Italy |
| `eprel.md` | EU Energy Label database (official energy class, kWh) |
| `safety-gate.md` | EU Safety Gate/RAPEX product recall database |
| `reparabilite-fr.md` | French repairability/durability index (mandatory, open data) |
| `ifixit.md` | Teardown scores, repair guides, spare parts |
| `output-schema.md` | JSON schema for structured agent output |

## Incognito Mode

```
/buy-incognito birthday gift for my wife
```

**Same pipeline** as `/buy` — same agents, same steps, same structured output — but writes nothing to disk:
- No reports saved
- No structured results saved
- No learnings updated
- No memory updated
- Results exist only in conversation memory
- After `/clear`, no trace remains

## Search Scope

- **Priority 1**: Italy and EU (no duties, fast shipping)
- **Priority 2**: Global (only if significant savings)
- Always calculated: price + shipping + duties/VAT toward Italy
- Amazon: all EU domains (it, de, fr, es, nl, be, pl, se, co.uk)

## Post-Purchase Workflow

1. Purchase confirmed -> report marked as `PURCHASED`, product added to `tracker/purchased.json`
2. After 2-4 weeks -> feedback requested (satisfaction, surprises, issues)
3. Feedback saved in report and fed back into agent learnings
4. Safety Gate/RAPEX monitored periodically for product recalls

## Stack

- **Runtime**: Claude Code (native multi-agent, no framework)
- **Agents**: 9 specialized Claude subagents with persistent learnings
- **Search**: WebSearch (API) + WebFetch (HTTP GET) + Python scrapers
- **Data**: Markdown (reports) + JSON (structured results) + CSV (price history)
- **Tracker**: Python 3.12 (stdlib only, zero external dependencies)
- **External dependencies**: none

## License

MIT
