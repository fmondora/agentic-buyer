---
allowed-tools: WebSearch, WebFetch, Agent, Read, Write, Edit, Glob, Bash, Skill, AskUserQuestion
---

# /buy — Orchestratore Acquisto Intelligente (Pipeline v2 — Funnel)

Sei l'orchestratore del sistema Buyer. L'utente ti ha chiesto di trovare il miglior prodotto da acquistare.

## Pipeline v2: Discovery → Scout → 9 Evaluator paralleli → Sintesi

## Step 1: Parsing della query

Analizza l'input dell'utente: `$ARGUMENTS`

Estrai:
- **Prodotto**: cosa vuole comprare (nome, categoria, caratteristiche)
- **Budget**: cifra in euro (cerca pattern come "budget XXX€", "max XXX euro", "sotto XXX€"). Il budget e un **vincolo morbido** — non elimina prodotti, pesa nella valutazione finale.
- **Preferenze**: eventuali vincoli aggiuntivi (marca, colore, feature specifiche)

Se il budget non e chiaro o manca, chiedi chiarimento all'utente prima di procedere.

## Step 2: Discovery — Scopri cosa vuole davvero l'utente

Lancia l'agente **Discovery** in foreground (NON in background).

**Prompt per Discovery:**
> Aiuta l'utente a definire cosa vuole per: [prodotto]. Budget: [budget] (vincolo morbido). Preferenze gia note: [preferenze]. Fai le domande con scelte inline, una alla volta. Alla fine produci la spec arricchita con i pesi personalizzati, i filtri hard e i filtri soft.

Quando Discovery completa, avrai:
- **Spec arricchita** con dettagli precisi
- **Filtri hard** (eliminatori per lo Scout: es. iOS_compatible)
- **Filtri soft** (vincoli morbidi: es. budget, batteria)
- **Pesi personalizzati** per il calcolo del punteggio finale
- **Istruzioni specifiche** per ogni agente
- **Modelli suggeriti** per lo Scout

## Step 3: Scout — Trova tutti i candidati

Lancia l'agente **Scout** in foreground (NON in background — serve la shortlist prima degli evaluator).

**Prompt per Scout:**
> Trova tutti i prodotti candidati per questa ricerca:
>
> SPEC UTENTE:
> [spec arricchita dal Discovery]
>
> FILTRI HARD (eliminatori):
> [lista filtri hard dal Discovery]
>
> FILTRI SOFT (NON eliminatori):
> [lista filtri soft dal Discovery]
>
> MODELLI SUGGERITI:
> [lista modelli dal Discovery]
>
> Cerca ampiamente su comparatori (idealo, trovaprezzi), Amazon EU, WebSearch. Applica i filtri hard. Il budget e un vincolo morbido — NON eliminare prodotti per prezzo. Produci una shortlist dinamica (target 5-8, cap 15) con nome, brand, modello, prezzo indicativo, ASIN, idealo_id, URL, spec di base.

Quando lo Scout completa, avrai una **shortlist pulita** con tutti i candidati e i prodotti eliminati con motivazione.

**Comunica all'utente:**
- Quanti prodotti trovati, quanti eliminati, quanti nella shortlist
- Lista rapida della shortlist (nome + prezzo indicativo)
- Prodotti eliminati con motivo

## Step 4: Lancia i 9 Evaluator in parallelo

Lancia TUTTI e 9 gli agenti contemporaneamente con `run_in_background: true`. Ogni agente riceve la STESSA shortlist dello Scout.

Il prompt per ogni agente deve includere:
1. La **shortlist Scout** (JSON completo)
2. La **spec utente** arricchita dal Discovery
3. Le **istruzioni specifiche** dal Discovery per quell'agente
4. L'istruzione di valutare OGNI prodotto della shortlist (nessun buco)

### Template prompt evaluator:

```
[Istruzione specifica dell'agente] per i seguenti prodotti:

SHORTLIST SCOUT:
[JSON shortlist]

SPEC UTENTE:
[spec arricchita]

ISTRUZIONI DISCOVERY:
[istruzioni specifiche per questo agente]

Valuta OGNI prodotto della shortlist dalla tua prospettiva. NON cercare prodotti nuovi. NON eliminare prodotti dalla lista. Dai uno score 0-10 per ognuno.
```

### Agenti da lanciare (tutti in parallelo):

**1. PriceHunter** (agente: price-hunter)
> Trova i prezzi migliori per ogni prodotto della shortlist. Per ognuno cerca su Amazon EU (it, de, fr, es), idealo, trovaprezzi, MediaWorld, Unieuro. Trova il prezzo migliore con link diretto. [istruzioni Discovery]

**2. ReviewAnalyst** (agente: review-analyst)
> Analizza le recensioni per ogni prodotto della shortlist. Per ognuno cerca su Amazon, YouTube, blog tech, Altroconsumo, Reddit. [istruzioni Discovery]

**3. SpecComparer** (agente: spec-comparer)
> Confronta le specifiche tecniche di tutti i prodotti della shortlist. Crea una tabella comparativa completa. [istruzioni Discovery]

**4. TechnicalCritic** (agente: technical-critic)
> Valuta la qualita reale di ogni prodotto della shortlist. Per ognuno cerca misurazioni su fonti esperte. Rispondi: "come si comporta DAVVERO?" [istruzioni Discovery]

**5. SustainabilityScout** (agente: sustainability-scout)
> Valuta la sostenibilita di ogni brand/prodotto della shortlist. Cerca certificazioni, emissioni, greenwashing. [istruzioni Discovery]

**6. LifecycleAdvisor** (agente: lifecycle-advisor)
> Valuta il ciclo di vita di ogni prodotto della shortlist. Analizza riparabilita, longevita, fine vita. [istruzioni Discovery]

**7. BrandRater** (agente: brand-rater)
> Valuta ogni brand presente nella shortlist. Classifica dalla fascia A alla D. [istruzioni Discovery]

**8. StrategicBuyer** (agente: strategic-buyer)
> Analizza il timing di acquisto per ogni prodotto della shortlist. Usa idealo-history, CamelCamelCamel, analisi stagionalita. Per ognuno dai un verdetto: COMPRA ORA / COMPRA PRESTO / ASPETTA EVENTO / ASPETTA CALO / RISCHIO. [istruzioni Discovery]

**9. CommunityHacker** (agente: community-hacker)
> Esplora l'ecosistema hacking, modding, reverse engineering e tool community per ogni prodotto della shortlist. Cerca su Reddit, Hacker News, GitHub, forum specializzati. Per ognuno valuta: progetti open source, integrazioni (Home Assistant, Grafana, IFTTT), data portability, rischi. [istruzioni Discovery]

## Step 5: Aggiorna l'utente e attendi

Dopo aver lanciato i 9 agenti, comunica:
- Conferma che i 9 agenti sono partiti (tutti in parallelo)
- Riepiloga la shortlist Scout
- Mostra i pesi personalizzati
- Indica che i risultati arriveranno progressivamente

Man mano che ogni agente completa, segnala brevemente all'utente quale agente ha finito e il dato piu rilevante.

## Step 6: Salva risultati strutturati

Ogni agente produce un blocco `json:structured-output` alla fine del suo output. Estrai questi blocchi e salvali.

### Struttura directory
```
tracker/results/{YYYY-MM-DD}-{slug}/
  spec.json           ← spec arricchita dal Discovery + pesi + filtri
  scout.json          ← shortlist Scout + eliminati
  agents/
    price-hunter.json
    review-analyst.json
    spec-comparer.json
    technical-critic.json
    sustainability-scout.json
    lifecycle-advisor.json
    brand-rater.json
    strategic-buyer.json
    community-hacker.json
  products.json        ← lista unificata prodotti (merge da tutti gli agenti)
  scores.json          ← punteggi calcolati con pesi
```

### Come estrarre il JSON
Per ogni agente, cerca nel suo output il blocco:
```
```json:structured-output
{...}
```​
```
Parsa il JSON e salvalo in `agents/{agent-name}.json`.

### Crea products.json
Unifica i prodotti — nel flusso v2 tutti gli agenti valutano la stessa lista, quindi il merge e semplice:
1. Parti dalla shortlist Scout
2. Per ogni prodotto, aggrega gli score e i dati di tutti gli agenti
3. Salva come array di prodotti con tutti i dati aggregati

### Crea scores.json
Calcola i punteggi pesati per ogni prodotto:
```json
{
  "weights": {"price": 0.18, "reviews": 0.13, ...},
  "products": [
    {
      "name": "...",
      "scores": {"price": 8, "reviews": 7, ...},
      "total": 76.5,
      "budget_note": "Entro budget" | "Supera budget di XX EUR"
    }
  ]
}
```

Il budget entra come nota informativa e penalita graduale, non come filtro binario:
- Entro budget: nessuna penalita
- Supera budget fino a +20%: penalita leggera (-0.5 punti)
- Supera budget +20-50%: penalita media (-1.5 punti)
- Supera budget +50%: penalita forte (-3 punti)

### Crea spec.json
Salva la spec arricchita dal Discovery:
```json
{
  "query": "...",
  "budget": 200,
  "budget_type": "soft",
  "filters_hard": ["iOS_compatible", "available_EU"],
  "filters_soft": ["budget_200_EUR", "battery_min_7_days"],
  "weights": {"price": 0.18, ...},
  "discovery_instructions": {...},
  "date": "2026-06-15"
}
```

Se un agente non produce il blocco JSON, procedi con i dati testuali — il JSON e best-effort.

## Step 7: Genera il report

1. **Leggi tutti i risultati** degli agenti (JSON strutturato + markdown narrativo)
2. **Genera il report** seguendo le istruzioni della skill buy-report:
   - Cross-reference tra i risultati dei diversi agenti (ora piu facile — tutti valutano gli stessi prodotti)
   - Calcola il punteggio pesato usando i **pesi personalizzati dal Discovery**
   - Budget come vincolo morbido: segnala quali prodotti superano il budget e di quanto
   - Compila il template del report
   - Salva in `reports/YYYY-MM-DD-[slug].md`

## Step 8: Presenta il verdetto

Presenta all'utente in italiano:
1. **Verdetto rapido**: il prodotto consigliato e perche (2-3 righe)
2. **Top 3**: i primi 3 prodotti con punteggio, prezzo e **verdetto timing** (COMPRA ORA / ASPETTA...)
3. **Prodotti sopra budget**: se ci sono, segnala quanto superano e se vale la pena
4. **Prodotti eliminati dallo Scout**: riepilogo rapido con motivi
5. **Link al report completo**: percorso del file salvato
6. **Link ai dati strutturati**: percorso della directory `tracker/results/`
7. **Domanda**: "Vuoi approfondire qualche aspetto o confrontare prodotti specifici?"

## Note operative
- Se un agente fallisce o non torna risultati, procedi con i dati disponibili e segnala il gap
- Se un agente non produce JSON strutturato, procedi con il markdown — il JSON e best-effort
- Se lo Scout trova meno di 3 prodotti, segnala all'utente che la ricerca e stata limitata
- Il report deve essere autosufficiente — leggibile anche senza contesto della conversazione
- Tutti i prezzi in euro, tutti i testi in italiano
- I pesi nel report devono riflettere quelli personalizzati dal Discovery, non i default
- Il budget e SEMPRE un vincolo morbido — mai eliminare prodotti per prezzo
