# Buyer — Sistema Multi-Agente per Acquisti Intelligenti

## Lingua
- Italiano sempre (output, report, commenti)
- Inglese solo per nomi tecnici e frontmatter YAML

## Convenzioni
- Report salvati in `reports/YYYY-MM-DD-[slug].md`
- Slug: nome prodotto kebab-case, max 40 caratteri
- Agenti lanciano in parallelo via Agent tool con `run_in_background: true`
- Ogni agente produce output strutturato in markdown
- La skill `buy-report` sintetizza i risultati e genera il report finale

## Flusso /buy
1. **Discovery** (foreground) — domande rapide con scelte inline per capire cosa vuole l'utente → produce spec arricchita + pesi personalizzati
2. **7 agenti** (parallelo, background) — cercano con la spec arricchita e le istruzioni specifiche del Discovery
3. **Sintesi** — calcola punteggi con i pesi personalizzati, genera report

## Agenti
8 agenti in `.claude/agents/`:
- **discovery** — interattivo, domande con scelte inline, personalizza pesi (foreground)
- price-hunter, review-analyst, spec-comparer, technical-critic, sustainability-scout, lifecycle-advisor, brand-rater (background, parallelo)

## Pesi sintesi finale (default — personalizzabili dal Discovery)
| Dimensione | Peso | Agente |
|---|---|---|
| Prezzo | 20% | PriceHunter |
| Recensioni | 15% | ReviewAnalyst |
| Specifiche + Energia | 15% | SpecComparer |
| Criticita tecnica | 10% | TechnicalCritic |
| Sostenibilita | 10% | SustainabilityScout |
| Ciclo di vita | 10% | LifecycleAdvisor |
| Reputazione brand | 20% | BrandRater |

I pesi vengono personalizzati dal Discovery in base alle risposte dell'utente (es: "cinema stanza buia" → Critica tecnica +5%, "brand importante" → Brand +5%).

## Playbook per sito
- In `.claude/agents/tools/` ci sono playbook riutilizzabili per navigare siti specifici
- Playbook disponibili: `amazon-eu.md`, `trovaprezzi.md`, `idealo.md`, `ebay.md`, `global-search.md`
- Gli agenti leggono i playbook rilevanti prima di cercare su un sito
- Per aggiungere un nuovo sito: creare un nuovo .md in `tools/`

## Scope ricerca
- **Priorita 1**: Italia e EU (nessun dazio, spedizione veloce)
- **Priorita 2**: Globale (solo se risparmio significativo)
- **Sempre calcolare**: prezzo + spedizione verso Italia + dazi/IVA import
- **Amazon**: cercare su TUTTI gli Amazon EU (it, de, fr, es, nl, be, pl, se, co.uk)

## Learnings
- Ogni agente ha un file `learnings` in `.claude/agents/learnings/[nome-agente].md`
- Gli agenti leggono i learnings PRIMA di cercare e li aggiornano DOPO
- I learnings accumulano: fonti affidabili, fonti problematiche, pattern di ricerca, note per categoria
- Non usare Playwright — solo WebSearch (API di ricerca) e WebFetch (HTTP GET)

## Gestione errori
- Agente senza risultati: segnala gap, procede con dati disponibili
- WebSearch rate limited: retry con delay, fallback WebFetch su URL noti
- WebFetch fallisce su sito JS-heavy: segnala nel learnings come fonte problematica, prosegui con altri
- Budget non parsabile: chiedi chiarimento
- Meno di 3 prodotti: amplia termini di ricerca
- Tutti falliscono: report errore con suggerimenti manuali
