# Buyer — Multi-Agent Smart Shopping System

A native Claude Code system that evaluates products through 8 specialized agents running in parallel. Every purchase is scored across 7 dimensions: price, reviews, technical specs, real-world performance, sustainability, lifecycle, and brand reputation.

## How it works

```
/buy bluetooth headphones budget 200€
```

The system:
1. **Discovery** — asks 5-6 quick questions to understand what you really need, then personalizes search weights
2. **7 agents in parallel** — search the web via WebSearch + WebFetch (no browser, no Playwright)
3. **Synthesis** — cross-references agents, calculates weighted scores, generates a comprehensive markdown report

The final report contains the full reasoning from all agents, not just the verdict. It serves as a reference to resume context in future sessions.

## Commands

| Command | What it does |
|---------|-------------|
| `/buy <product>` | Full research with 8 agents, generates report |
| `/buy-incognito <product>` | Same as `/buy` but leaves no trace (no report, no learnings, no memory) |
| `/track add <product>` | Add a product to the price tracker |
| `/track check` | Check prices for all tracked products |
| `/track list` | Show the watchlist |
| `/track history <id>` | Price history for a product |

## Architecture

```
.claude/
  commands/
    buy.md              # Main orchestrator
    buy-incognito.md    # Incognito mode (zero traces)
    track.md            # Price tracker
  agents/
    discovery.md        # Interactive, personalizes the search
    price-hunter.md     # Finds prices on comparators and shops
    review-analyst.md   # Analyzes reviews (Amazon, YouTube, forums)
    spec-comparer.md    # Compares technical specifications
    technical-critic.md # Evaluates real-world performance vs marketing
    sustainability-scout.md  # Sustainability, emissions, greenwashing
    lifecycle-advisor.md     # Repairability, longevity, end-of-life
    brand-rater.md      # Brand reputation A-D, ethics, local support
    learnings/          # Persistent memory per agent
    tools/              # Site playbooks (Amazon, idealo, etc.)
  skills/
    buy-report/         # Template and logic for the final report
reports/                # Generated reports (YYYY-MM-DD-slug.md)
tracker/                # Python price tracker (stdlib only)
```

## Agents

### Discovery (foreground)
Interactive agent that asks numbered inline-choice questions. Produces an enriched spec and customizes weights based on answers (e.g., "durability matters" -> Lifecycle +10%, Price -10%).

### 7 Research Agents (parallel, background)

| Agent | What it searches | Default weight |
|-------|-----------------|---------------|
| **PriceHunter** | Prices on Amazon EU, idealo, trovaprezzi, eBay, specialized shops | 20% |
| **ReviewAnalyst** | Reviews on Amazon, YouTube, forums, Reddit, consumer reports | 15% |
| **SpecComparer** | Technical datasheets, comparison tables, energy ratings | 15% |
| **TechnicalCritic** | Real-world performance vs spec marketing, independent measurements | 10% |
| **SustainabilityScout** | Certifications, CO2, biodiversity, greenwashing detection | 10% |
| **LifecycleAdvisor** | Repairability, spare parts, warranty, resale value, end-of-life | 10% |
| **BrandRater** | Reliability, local support, ethics, local vs offshore production | 20% |

Weights are customized by Discovery for each search.

## Learnings

Each agent has a `learnings` file that accumulates experience across sessions:
- Reliable and problematic sources
- Effective search patterns per category
- Category-specific notes (e.g., "Samsung doesn't support Dolby Vision", "TCL throttles HDR in EU")

Learnings are read BEFORE each search and updated AFTER.

## Site Playbooks

Reusable instructions in `.claude/agents/tools/` for navigating specific sites:
- `amazon-eu.md` — all EU domains, ASIN-based search
- `trovaprezzi.md` — Italian price comparator
- `idealo.md` — EU price comparator
- `ebay.md` — auctions and buy-it-now
- `global-search.md` — worldwide search with duty/VAT calculation

## Price Tracker

Python script (stdlib only, zero dependencies) that monitors prices over time:

```bash
# Check all prices
python3.12 tracker/check_prices.py check

# Add a product
python3.12 tracker/check_prices.py add <id> <name> <url> <budget> <alert>

# Price history
python3.12 tracker/check_prices.py history <id>
```

Can be configured with cron for daily automatic checks.

## Incognito Mode

```
/buy-incognito birthday gift for my wife
```

Identical to `/buy` but:
- Does not save reports to disk
- Does not update agent learnings
- Does not update project memory
- Results exist only in the current conversation
- After `/clear`, no trace remains

Useful for: gifts, private purchases, exploratory comparisons.

## Search Scope

- **Priority 1**: Italy and EU (no duties, fast shipping)
- **Priority 2**: Global (only if significant savings)
- Always calculated: price + shipping + duties/VAT
- Amazon: all EU domains (it, de, fr, es, nl, be, pl, se, co.uk)

## Success Case Tracking

When a purchase is confirmed:
1. The report is marked as `PURCHASED`
2. After 2-4 weeks, feedback is requested
3. Feedback feeds back into agent learnings

## Stack

- **Runtime**: Claude Code (native, no framework)
- **Search**: WebSearch (API) + WebFetch (HTTP GET)
- **Tracker**: Python 3.12 (stdlib only)
- **Storage**: Markdown + JSON + CSV
- **External dependencies**: zero

## License

MIT
