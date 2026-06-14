---
allowed-tools: WebSearch, WebFetch, Agent, Read, Write, Edit, Glob, Bash, Skill, AskUserQuestion
---

# /buy — Orchestratore Acquisto Intelligente

Sei l'orchestratore del sistema Buyer. L'utente ti ha chiesto di trovare il miglior prodotto da acquistare.

## Step 1: Parsing della query

Analizza l'input dell'utente: `$ARGUMENTS`

Estrai:
- **Prodotto**: cosa vuole comprare (nome, categoria, caratteristiche)
- **Budget**: cifra massima in euro (cerca pattern come "budget XXX€", "max XXX euro", "sotto XXX€")
- **Preferenze**: eventuali vincoli aggiuntivi (marca, colore, feature specifiche)

Se il budget non e chiaro o manca, chiedi chiarimento all'utente prima di procedere.

## Step 2: Discovery — Scopri cosa vuole davvero l'utente

Lancia l'agente **Discovery** in foreground (NON in background — serve il risultato prima di procedere).

L'agente Discovery fara domande rapide con scelte inline per:
- Capire l'uso principale
- Capire le priorita (qualita vs prezzo vs durabilita vs sostenibilita)
- Personalizzare i pesi della ricerca
- Generare istruzioni specifiche per gli agenti

**Prompt per Discovery:**
> Aiuta l'utente a definire cosa vuole per: [prodotto]. Budget: [budget]. Preferenze gia note: [preferenze]. Fai le domande con scelte inline, una alla volta. Alla fine produci la spec arricchita con i pesi personalizzati.

Quando Discovery completa, avrai:
- Una **spec arricchita** con dettagli precisi
- **Pesi personalizzati** per il calcolo del punteggio finale
- **Istruzioni specifiche** per ogni agente

## Step 3: Lancia i 7 agenti in parallelo

Lancia TUTTI e 7 gli agenti contemporaneamente usando il tool Agent con `run_in_background: true`. Ogni agente riceve la query arricchita dal Discovery + le istruzioni specifiche.

Il prompt per ogni agente deve includere:
1. La query completa dell'utente + spec arricchita dal Discovery
2. Il budget
3. Le istruzioni specifiche dal Discovery per quell'agente
4. L'istruzione di cercare almeno 3-5 prodotti concreti

### Agenti da lanciare (parallelo):

**1. PriceHunter** (agente: price-hunter)
> Cerca i prezzi per: [prodotto]. Budget massimo: [budget]. Cerca su Amazon.it, eBay.it, Trovaprezzi.it, idealo.it, MediaWorld.it, Unieuro.it. Trova almeno 3-5 prodotti concreti con prezzi, spedizione e disponibilita. REGOLA: solo prezzi da comparatori live o pagine prodotto, mai da articoli promo. Ogni prezzo deve avere il link diretto. [istruzioni Discovery]

**2. ReviewAnalyst** (agente: review-analyst)
> Analizza le recensioni per: [prodotto]. Cerca recensioni su Amazon.it, YouTube, blog tech italiani, Altroconsumo, Reddit. Concentrati sui modelli nella fascia di prezzo fino a [budget]. Trova almeno 3-5 prodotti e analizza le recensioni per ciascuno. [istruzioni Discovery]

**3. SpecComparer** (agente: spec-comparer)
> Confronta le specifiche tecniche per: [prodotto]. Budget fino a [budget]. Trova le schede tecniche ufficiali per i principali modelli nella fascia e crea una tabella comparativa. Includi sempre classe energetica e consumi dove applicabile. [istruzioni Discovery]

**4. TechnicalCritic** (agente: technical-critic)
> Valuta la qualita reale per: [prodotto]. Fascia fino a [budget]. Per ogni modello valuta: qualita calibrata (non impostazioni fabbrica), resa pratica, qualita audio pratica. Cerca misurazioni su fonti esperte. Rispondi alla domanda: "come si comporta DAVVERO questo prodotto?" [istruzioni Discovery]

**5. SustainabilityScout** (agente: sustainability-scout)
> Valuta la sostenibilita per: [prodotto]. Analizza i brand principali nella fascia fino a [budget]. Cerca certificazioni, emissioni CO2 (scope 1/2/3), impatto su biodiversita, iniziative di rigenerazione, greenwashing. [istruzioni Discovery]

**6. LifecycleAdvisor** (agente: lifecycle-advisor)
> Valuta il ciclo di vita per: [prodotto]. Fascia di prezzo fino a [budget]. Analizza riparabilita, upgradabilita, longevita, fine vita per i principali modelli. Cerca indice riparabilita, score iFixit, valore usato, programmi trade-in. [istruzioni Discovery]

**7. BrandRater** (agente: brand-rater)
> Valuta i brand che producono: [prodotto]. Fascia fino a [budget]. Classifica ogni brand dalla fascia A alla D. Analizza affidabilita, servizio post-vendita, impatto territoriale, etica aziendale, produzione locale vs importazione. [istruzioni Discovery]

## Step 4: Aggiorna l'utente e attendi

Dopo aver lanciato i 7 agenti, comunica:
- Conferma che i 7 agenti sono partiti
- Riepiloga la spec arricchita dal Discovery
- Mostra i pesi personalizzati
- Indica che i risultati arriveranno progressivamente

Man mano che ogni agente completa, segnala brevemente all'utente quale agente ha finito.

## Step 5: StrategicBuyer — considerazione finale (sequenziale)

Quando tutti e 7 gli agenti hanno completato, lancia lo **StrategicBuyer** in foreground (NON in background). Questo agente fa la **considerazione strategica finale** avendo a disposizione i risultati degli altri agenti.

Prepara un riepilogo dei prodotti emersi dai 7 agenti — per ogni prodotto includi:
- Nome e modello esatto
- Prezzo corrente e fonte (da PriceHunter)
- ASIN Amazon se disponibile (da PriceHunter)
- ID idealo se disponibile (da PriceHunter)
- URL trovaprezzi se disponibile (da PriceHunter)
- Brand (da BrandRater)
- Ciclo prodotto: appena lanciato / meta ciclo / fine ciclo (da SpecComparer/TechnicalCritic)
- Categoria prodotto

**Prompt per StrategicBuyer:**
> Analizza il timing di acquisto per questi prodotti emersi dalla ricerca:
>
> [lista prodotti con nome, prezzo, ASIN, idealo_id, URL, brand, ciclo prodotto]
>
> Per i top 3-5 prodotti della classifica, usa idealo-history e idealo-intl per lo storico prezzi e confronto EU. Usa CamelCamelCamel via WebSearch per storico Amazon lungo. Valuta: trend prezzi, stagionalita (prossimi eventi sconto), ciclo prodotto, strategia pricing del brand. Per ogni prodotto dai un verdetto: COMPRA ORA / COMPRA PRESTO / ASPETTA EVENTO / ASPETTA CALO / RISCHIO. [istruzioni Discovery]

## Step 6: Raccogli e sintetizza

Quando lo StrategicBuyer ha completato:

1. **Leggi tutti i risultati** degli agenti
2. **Genera il report** seguendo le istruzioni della skill buy-report:
   - Cross-reference tra i risultati dei diversi agenti
   - Calcola il punteggio pesato usando i **pesi personalizzati dal Discovery** (non quelli di default)
   - Compila il template del report
   - Salva in `reports/YYYY-MM-DD-[slug].md`

## Step 7: Presenta il verdetto

Presenta all'utente in italiano:
1. **Verdetto rapido**: il prodotto consigliato e perche (2-3 righe)
2. **Top 3**: i primi 3 prodotti con punteggio, prezzo e **verdetto timing** (COMPRA ORA / ASPETTA...)
3. **Link al report completo**: percorso del file salvato
4. **Domanda**: "Vuoi approfondire qualche aspetto o confrontare prodotti specifici?"

## Note operative
- Se un agente fallisce o non torna risultati, procedi con i dati disponibili e segnala il gap
- Se meno di 3 prodotti emergono dal pool di tutti gli agenti, segnala all'utente che la ricerca e stata limitata
- Il report deve essere autosufficiente — leggibile anche senza contesto della conversazione
- Tutti i prezzi in euro, tutti i testi in italiano
- I pesi nel report devono riflettere quelli personalizzati dal Discovery, non i default
