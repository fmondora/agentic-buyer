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

## Playbook per sito e database pubblici
- In `.claude/agents/tools/` ci sono playbook riutilizzabili per navigare siti e database specifici
- **Siti e-commerce**: `amazon-eu.md`, `trovaprezzi.md`, `idealo.md`, `ebay.md`, `global-search.md`
- **Database pubblici EU**:
  - `eprel.md` — EU Energy Label: classe energetica, consumo kWh (usato da SpecComparer, SustainabilityScout)
  - `safety-gate.md` — Safety Gate/RAPEX: richiami prodotto EU, alert sicurezza (usato da BrandRater)
  - `reparabilite-fr.md` — Indice de reparabilite/durabilite francese: score 0-10 obbligatorio (usato da LifecycleAdvisor)
- **Riparazione e teardown**:
  - `ifixit.md` — iFixit: teardown, score riparabilita, guide riparazione passo-passo (usato da LifecycleAdvisor)
- Gli agenti leggono i playbook rilevanti prima di cercare su un sito
- Per aggiungere un nuovo sito/database: creare un nuovo .md in `tools/`

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

## Report — Contenuto e struttura
- Il report MD deve contenere TUTTO il reasoning degli agenti, non solo il verdetto
- Obiettivo: il report e autosufficiente per riprendere il contesto in futuro
- Includere: analisi dettagliate di ogni agente, cross-reference, trade-off, fonti con link
- Il report e il "cervello" della ricerca — deve essere ricco, non riassuntivo

## Acquisti completati (success cases)
- Quando l'utente conferma un acquisto, segnare nel report: `## Status: ACQUISTATO [data]`
- Aggiungere il prodotto scelto e il prezzo pagato
- **Aggiungere il prodotto a `tracker/purchased.json`** con brand, modello, prezzo, data, categoria
- Dopo 2-4 settimane, chiedere feedback sull'acquisto (soddisfazione, sorprese, problemi)
- Salvare il feedback nel report come `## Feedback post-acquisto [data]`
- I success case alimentano i learnings degli agenti (es: "utente soddisfatto di X per motivo Y")

## Monitoraggio post-acquisto
- `/track safety` — controlla Safety Gate/RAPEX per tutti i prodotti acquistati
- `/track safety <id>` — controlla solo un prodotto specifico
- Il registro acquisti e in `tracker/purchased.json`
- Safety Gate va controllato periodicamente (consigliato: mensile) per richiami/alert su prodotti posseduti

## Gestione errori
- Agente senza risultati: segnala gap, procede con dati disponibili
- WebSearch rate limited: retry con delay, fallback WebFetch su URL noti
- WebFetch fallisce su sito JS-heavy: segnala nel learnings come fonte problematica, prosegui con altri
- Budget non parsabile: chiedi chiarimento
- Meno di 3 prodotti: amplia termini di ricerca
- Tutti falliscono: report errore con suggerimenti manuali
