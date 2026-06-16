# Pipeline v2 — Funnel Design

**Data**: 2026-06-15
**Stato**: Approvato
**Problema**: Gli agenti girano alla cieca in parallelo, ognuno cerca prodotti indipendentemente. Risultato: lavoro sprecato su prodotti poi eliminati (Samsung/Xiaomi incompatibili iOS), buchi di copertura (Helio Strap trovato solo da 1 agente), duplicazione di ricerca.

## Architettura

```
Discovery (interattivo, foreground)
    |
    v
  spec + pesi + filtri hard (es: iOS, categoria)
    |
    v
Scout (1 agente, foreground)
    |
    v
  shortlist dinamica (target 5-8, cap 15)
  per ogni prodotto: nome, brand, modello, prezzo indicativo, ASIN, idealo_id, link, spec base
  filtri hard applicati
  budget NON e filtro (e un vincolo morbido nella pesatura finale)
    |
    v
8 Evaluator TUTTI in parallelo (background)
  PriceHunter, ReviewAnalyst, SpecComparer, TechnicalCritic,
  SustainabilityScout, LifecycleAdvisor, BrandRater, StrategicBuyer
    |
    v
Sintesi (foreground)
  punteggi pesati con budget come vincolo morbido, report
```

## Cambiamenti rispetto a v1

| Aspetto | v1 (oggi) | v2 (funnel) |
|---|---|---|
| Ricerca prodotti | Ogni agente cerca i suoi | Scout unico cerca tutti |
| Filtri hard | Nessuno (eliminazione a posteriori) | Scout applica filtri hard prima della valutazione |
| Budget | Filtro eliminatorio | Vincolo morbido nella pesatura finale |
| Evaluator | Cercano + valutano | Solo valutano (ricevono shortlist) |
| StrategicBuyer | Sequenziale dopo i 7 | In parallelo con gli altri 7 |
| Copertura prodotti | Incompleta (buchi cross-agente) | Completa (tutti valutano la stessa lista) |
| Lavoro sprecato | Alto (prodotti eliminati dopo analisi completa) | Minimo (filtri hard applicati prima) |

## Scout — Nuovo agente

### Responsabilita
1. Ricevere spec + filtri hard dal Discovery
2. Cercare ampiamente su tutte le fonti (WebSearch, scraper, comparatori)
3. Applicare filtri hard (compatibilita, disponibilita, categoria corretta)
4. Produrre shortlist dinamica (target 5-8, cap 15)
5. Per ogni prodotto: nome, brand, modello, prezzo indicativo, ASIN, idealo_id, link, spec di base

### NON fa
- Non valuta qualita, sostenibilita, brand, ciclo vita
- Non elimina per budget (budget e vincolo morbido)
- Non ordina per preferenza

### Filtri hard (eliminatori)
- Compatibilita tecnica (es: iOS per utente iPhone)
- Disponibilita (esiste? si compra in EU?)
- Categoria corretta (es: band, non smartwatch 50mm)
- Qualsiasi filtro esplicito dal Discovery

### Filtri morbidi (NON eliminatori)
- Budget (entra nella pesatura, non elimina)
- Batteria (dimensione di valutazione)
- Peso/dimensioni (dimensione di valutazione)

### Tools
- WebSearch, WebFetch, Read, Edit, Bash (scraper)
- Legge playbook in `.claude/agents/tools/`
- Legge learnings da tutti gli agenti per fonti note

### Output
Shortlist JSON con struttura:

```json
{
  "filters_applied": ["iOS_compatible", "available_EU", "category_fitness_band"],
  "filters_soft": ["budget_200_EUR"],
  "total_found": 12,
  "shortlist": [
    {
      "name": "Garmin Vivosmart 5",
      "brand": "Garmin",
      "model": "Vivosmart 5",
      "price_indicative": 125,
      "currency": "EUR",
      "asin": "B09WF38HK4",
      "idealo_id": "201919307",
      "url": "https://www.amazon.it/dp/B09WF38HK4",
      "spec_summary": "PPG HR, Body Battery (HRV), VO2max, SpO2, 5ATM, 7gg batteria",
      "year_launched": 2022,
      "notes": "Modello 2022, nessun successore annunciato"
    }
  ],
  "eliminated": [
    {
      "name": "Samsung Galaxy Fit 3",
      "reason": "Incompatibile con iPhone (filtro hard: iOS_compatible)"
    }
  ]
}
```

## Evaluator — Ruolo aggiornato

Ogni evaluator riceve la shortlist dello Scout e valuta SOLO quei prodotti dalla sua prospettiva. Non cerca piu prodotti autonomamente.

### Prompt template per evaluator (v2)

```
Valuta i seguenti prodotti dalla prospettiva di [dimensione]:

SHORTLIST:
[JSON shortlist dallo Scout]

SPEC UTENTE:
[spec arricchita dal Discovery]

Per OGNI prodotto nella shortlist, produci:
- Score 0-10
- Analisi dettagliata
- Fonti

NON cercare altri prodotti. Valuta SOLO quelli nella shortlist.
[istruzioni specifiche dal Discovery]
```

### Cambiamenti per agente

| Agente | Cosa cambia |
|---|---|
| PriceHunter | Non cerca prodotti. Riceve la lista e trova i prezzi migliori per ciascuno su tutti i canali |
| ReviewAnalyst | Non cerca prodotti. Riceve la lista e cerca recensioni per ciascuno |
| SpecComparer | Non cerca prodotti. Riceve la lista e confronta le spec di quelli specifici |
| TechnicalCritic | Non cerca prodotti. Riceve la lista e valuta la qualita reale di ciascuno |
| SustainabilityScout | Non cerca prodotti. Riceve la lista e valuta sostenibilita dei brand presenti |
| LifecycleAdvisor | Non cerca prodotti. Riceve la lista e valuta ciclo vita di ciascuno |
| BrandRater | Non cerca prodotti. Riceve la lista e classifica i brand presenti |
| StrategicBuyer | Ora in parallelo. Riceve la lista con ASIN/idealo_id e analizza timing per ciascuno |

## Discovery — Cosa cambia

Il Discovery produce in piu:
- **Filtri hard**: lista esplicita di filtri eliminatori (es: `["iOS_compatible"]`)
- **Modelli suggeriti**: lista di modelli da cercare (come oggi, ma piu esplicita)
- Budget rimane nell'output ma etichettato come vincolo morbido

## Sintesi — Cosa cambia

- Il budget entra come penalita graduale nel punteggio, non come filtro binario
- Esempio: prodotto a 250 EUR con budget 200 EUR → penalita proporzionale al superamento (-X punti), non eliminazione
- Tutti i prodotti hanno score da tutti gli agenti → nessun buco di copertura
- La tabella finale e completa e confrontabile

## Orchestratore /buy — Nuovo flusso

```
Step 1: Parsing query (come oggi)
Step 2: Discovery (come oggi, + filtri hard nell'output)
Step 3: Scout (NUOVO — foreground)
Step 4: 8 Evaluator in parallelo (background) — tutti ricevono la stessa shortlist
Step 5: Sintesi + salvataggio risultati (come oggi)
Step 6: Report (come oggi)
Step 7: Verdetto (come oggi)
```

## File da creare/modificare

| File | Azione |
|---|---|
| `.claude/agents/scout.md` | CREARE — nuovo agente Scout |
| `.claude/agents/discovery.md` | MODIFICARE — aggiungere filtri hard nell'output |
| `.claude/agents/price-hunter.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/review-analyst.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/spec-comparer.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/technical-critic.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/sustainability-scout.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/lifecycle-advisor.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/brand-rater.md` | MODIFICARE — ruolo evaluator puro |
| `.claude/agents/strategic-buyer.md` | MODIFICARE — ora in parallelo, riceve shortlist Scout |
| `.claude/commands/buy.md` | RISCRIVERE — nuovo flusso funnel |
| `.claude/commands/buy-incognito.md` | RISCRIVERE — allineare a buy.md |
| `CLAUDE.md` | AGGIORNARE — documentazione flusso v2 |

## Rischi e mitigazioni

| Rischio | Mitigazione |
|---|---|
| Scout non trova un prodotto rilevante | Scout legge learnings di tutti gli agenti + modelli suggeriti dal Discovery |
| Scout troppo lento (fase sequenziale) | Scout usa scraper + WebSearch in parallelo, target 3-5 minuti |
| Evaluator trovano info su prodotti non in lista | Possono segnalare "prodotto alternativo trovato" ma non cambiare la shortlist |
| Budget come vincolo morbido confonde l'utente | Report segnala chiaramente quali prodotti superano il budget e di quanto |
