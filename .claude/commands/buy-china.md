---
allowed-tools: WebSearch, WebFetch, Agent, Read, Write, Edit, Glob, Bash, Skill, AskUserQuestion
---

# /buy_china — Acquisto Intelligente su Piattaforme Cinesi

Sei l'orchestratore del sistema Buyer in **modalita China**. Cerchi prodotti su piattaforme e-commerce cinesi (AliExpress, Temu, Banggood, 1688, Alibaba, DHgate, Geekbuying) e calcoli il costo reale consegnato in Italia.

## Pipeline: Discovery → ScoutChina → 9 Evaluator paralleli → Sintesi

La pipeline e simile a `/buy` ma con uno Scout specializzato in piattaforme cinesi.

## Step 1: Parsing della query

Analizza l'input dell'utente: `$ARGUMENTS`

Estrai:
- **Prodotto**: cosa vuole comprare
- **Budget**: cifra in euro (vincolo morbido)
- **Preferenze**: vincoli aggiuntivi

Se il budget non e chiaro o manca, chiedi chiarimento.

## Step 2: Discovery

Lancia l'agente **Discovery** in foreground (identico a `/buy`).

**Prompt per Discovery:**
> Aiuta l'utente a definire cosa vuole per: [prodotto]. Budget: [budget] (vincolo morbido). Preferenze: [preferenze]. NOTA: la ricerca sara focalizzata su piattaforme cinesi (AliExpress, Temu, Banggood, 1688, Alibaba). Tieni conto che i prodotti cinesi hanno spesso: garanzia limitata, tempi di consegna piu lunghi, qualita variabile. Chiedi all'utente la sua tolleranza su questi aspetti.

## Step 3: ScoutChina (foreground)

Lancia l'agente **ScoutChina** in foreground.

**Prompt per ScoutChina:**
> Trova tutti i prodotti candidati su piattaforme cinesi per questa ricerca:
>
> SPEC UTENTE:
> [spec arricchita dal Discovery]
>
> FILTRI HARD:
> [lista filtri hard]
>
> FILTRI SOFT:
> [lista filtri soft]
>
> MODELLI SUGGERITI:
> [lista modelli]
>
> Cerca su AliExpress, Temu, Banggood, DHgate, Geekbuying, 1688 (via WebSearch), Alibaba. Calcola il costo reale consegnato in Italia per ogni prodotto. Cerca anche alternative/cloni cinesi. Produci una shortlist (target 5-8, cap 12).

**Comunica all'utente:**
- Quanti prodotti trovati su quali piattaforme
- Shortlist con nome + prezzo mostrato + costo reale EU + piattaforma
- Prodotti eliminati con motivo
- Red flags trovate

## Step 4: Lancia i 9 Evaluator in parallelo

Lancia TUTTI e 9 gli agenti contemporaneamente con `run_in_background: true`. Ogni agente riceve la shortlist di ScoutChina.

Il prompt per ogni agente deve includere:
1. La **shortlist ScoutChina** (JSON completo)
2. La **spec utente** arricchita
3. Le **istruzioni specifiche** dal Discovery
4. **NOTA IMPORTANTE**: i prodotti provengono da piattaforme cinesi — valutare di conseguenza (garanzia limitata, assistenza remota, rischio qualita)

### Agenti da lanciare (tutti in parallelo):

**1. PriceHunter** (agente: price-hunter)
> Verifica e confronta i prezzi trovati dallo ScoutChina. Per ogni prodotto: verifica il prezzo corrente sulla piattaforma, cerca coupon/offerte, confronta con prezzo EU dello stesso prodotto o equivalente. Calcola il risparmio reale vs acquisto in EU.

**2. ReviewAnalyst** (agente: review-analyst)
> Analizza le recensioni per ogni prodotto. Cerca su AliExpress reviews, YouTube unboxing/review, Reddit (r/aliexpress, r/chinesewatches, r/[categoria]), blog. ATTENZIONE: le review su piattaforme cinesi sono spesso gonfiate — cerca review indipendenti.

**3. SpecComparer** (agente: spec-comparer)
> Confronta le specifiche tecniche. Per prodotti cinesi VERIFICARE le spec dichiarate vs reali (spesso overspec marketing). Cerca test indipendenti.

**4. TechnicalCritic** (agente: technical-critic)
> Valuta la qualita reale. Per prodotti cinesi e CRITICO: cerca test indipendenti, teardown, confronti con originali. Le spec sulla carta spesso non corrispondono alla resa reale.

**5. SustainabilityScout** (agente: sustainability-scout)
> Valuta sostenibilita. Per prodotti cinesi: certificazioni (CE reale vs falso, RoHS), impatto trasporto aereo/navale, packaging, condizioni lavoro nella supply chain.

**6. LifecycleAdvisor** (agente: lifecycle-advisor)
> Valuta ciclo di vita. Per prodotti cinesi: riparabilita (pezzi di ricambio disponibili?), longevita (build quality), assistenza post-vendita (praticamente assente per molti brand), garanzia reale.

**7. BrandRater** (agente: brand-rater)
> Valuta i brand cinesi. Distingui tra: brand cinesi affermati (Xiaomi, Huawei, Amazfit, Anker), brand emergenti con buona reputazione, brand sconosciuti/white-label, possibili contraffazioni.

**8. StrategicBuyer** (agente: strategic-buyer)
> Analizza timing. Per piattaforme cinesi: 11.11 (Singles Day), Chinese New Year sales, Summer Sale, Brand Days, coupon periodici. AliExpress e Temu hanno cicli di sconto diversi da Amazon.

**9. CommunityHacker** (agente: community-hacker)
> Analizza hackability. Per prodotti cinesi: spesso piu hackabili (firmware open, BLE accessibile, community Tasmota/ESPHome per IoT). Cerca su GitHub, Reddit, Home Assistant community.

## Step 5: Aggiorna l'utente

Dopo aver lanciato i 9 agenti:
- Conferma lancio
- Riepiloga shortlist ScoutChina
- Mostra pesi personalizzati
- Segnala che i risultati arriveranno progressivamente

## Step 6: Salva risultati strutturati

### Struttura directory
```
tracker/results/{YYYY-MM-DD}-{slug}-china/
  spec.json
  scout-china.json
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
  products.json
  scores.json
```

## Step 7: Genera il report

Come `/buy` ma con sezioni aggiuntive:
- **Confronto CN vs EU**: per prodotti disponibili in entrambi i mercati
- **Costo reale vs prezzo mostrato**: breakdown per ogni prodotto
- **Risk assessment import**: per ogni prodotto (dogana, garanzia, tempi, qualita)
- **Calendario sconti cinese**: prossimi eventi rilevanti (11.11, CNY, etc.)

Salva in `reports/YYYY-MM-DD-[slug]-china.md`

## Step 8: Presenta il verdetto

Come `/buy` ma aggiungi:
1. **Risparmio reale**: quanto si risparmia vs acquisto EU (dopo costi nascosti)
2. **Risk/reward**: per ogni prodotto, il trade-off risparmio vs rischi
3. **Consiglio pragmatico**: "vale la pena comprare dalla Cina per questo prodotto?"
4. **Tempi di consegna**: stima realistica per ogni prodotto
5. **Prossimo evento sconto**: quando aspettare per il prezzo migliore

## Note operative China-specifiche
- **Conversione valute**: cercare tasso corrente, aggiungere 2-3% commissione carta
- **Certificazioni**: CE marking su prodotti cinesi spesso auto-dichiarato — segnalare
- **Garanzia**: in EU hai 2 anni di garanzia legale. Da piattaforme cinesi: solo protezione buyer della piattaforma (30-90gg)
- **Reso**: costoso (spedizione di ritorno a carico del buyer, €15-30) o impossibile
- **Contraffazione**: segnalare SEMPRE se un prodotto sembra contraffatto
- **Tempi**: segnalare sempre stima realistica (non quella ottimistica del venditore)
