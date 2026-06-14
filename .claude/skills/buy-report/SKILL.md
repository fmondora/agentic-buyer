---
name: buy-report
description: Sintetizza i risultati degli 8 agenti e genera il report finale di acquisto
---

# Skill: Generazione Report Acquisto

## Quando usare
Questa skill viene invocata dall'orchestratore `/buy` dopo che tutti gli 8 agenti hanno completato il loro lavoro. Ricevi i risultati grezzi degli 8 agenti e produci un report finale strutturato.

## Input atteso
Ricevi i finding di 8 agenti:
1. **PriceHunter** — prezzi e disponibilita
2. **ReviewAnalyst** — recensioni e sentiment
3. **SpecComparer** — specifiche tecniche e dati energetici
4. **TechnicalCritic** — qualita visiva reale, calibrazione, Filmmaker Mode, HDR, motion
5. **SustainabilityScout** — sostenibilita, emissioni, biodiversita
6. **LifecycleAdvisor** — riparabilita, upgradabilita, fine vita, longevita
7. **BrandRater** — reputazione brand, impatto territoriale, etica
8. **StrategicBuyer** — timing acquisto, trend prezzi, stagionalita, ciclo prodotto

## Procedura di sintesi

### Step 1: Identifica i prodotti
Crea la lista unificata dei prodotti trovati dagli agenti. Unisci prodotti duplicati citati da agenti diversi.

### Step 2: Cross-reference
Rispondi a queste domande per ogni prodotto:
- Il piu economico ha buone recensioni?
- Quello con le migliori specifiche e anche riparabile?
- Il brand piu etico offre un buon rapporto qualita/prezzo?
- Il prodotto piu sostenibile ha specifiche competitive?
- Quello con il miglior ciclo di vita e anche ben recensito?
- Il prodotto con le migliori spec sulla carta rende bene anche calibrato? (criticita tecnica)
- Quello consigliato dal critico tecnico ha un prezzo ragionevole e un brand affidabile?

### Step 3: Calcolo punteggio pesato
Per ogni prodotto, calcola un punteggio /100 usando questi pesi:

| Dimensione | Peso | Come calcolare |
|---|---|---|
| Prezzo | 18% | Il piu economico = 10, scala proporzionale al budget |
| Recensioni | 13% | Media recensioni normalizzata a 10 |
| Specifiche + Energia | 13% | Score tecnico dell'agente, bonus per classe energetica alta |
| Criticita tecnica | 10% | Score del TechnicalCritic (qualita reale pannello, HDR, Filmmaker Mode) |
| Sostenibilita | 8% | Score sostenibilita dell'agente |
| Ciclo di vita | 8% | Score ciclo di vita dell'agente |
| Brand | 18% | Score brand dell'agente (fascia A=10, B=7.5, C=5, D=2.5) |
| Timing | 12% | Score StrategicBuyer (COMPRA ORA=10, COMPRA PRESTO=8, ASPETTA EVENTO=5, ASPETTA CALO=3, RISCHIO=1) |

**Formula**: `Totale = (Prezzo * 0.18 + Recensioni * 0.13 + Spec * 0.13 + Critica * 0.10 + Sostenibilita * 0.08 + CicloVita * 0.08 + Brand * 0.18 + Timing * 0.12) * 10`

### Step 4: Genera il report
Usa il template in `templates/report-template.md` come struttura. Compila ogni sezione con i dati raccolti.

Regole per la compilazione:
- **Verdetto rapido**: max 2 righe, prodotto consigliato + motivazione principale
- **Tabella riassuntiva**: un riga per prodotto, punteggi per dimensione + totale
- **Analisi dettagliata**: riassumi i finding di ogni agente, evidenzia solo i dati piu rilevanti
- **Classifica finale**: ordine decrescente per punteggio, con motivazione per ogni posizione
- **Dopo l'acquisto**: consigli pratici e specifici dal LifecycleAdvisor
- **Fonti**: lista di tutti i link e riferimenti usati dagli agenti

### Step 5: Salva il report
Salva il report in `reports/YYYY-MM-DD-[slug].md` dove:
- `YYYY-MM-DD` = data odierna
- `[slug]` = nome prodotto in kebab-case, max 40 caratteri

## Output
- Il report markdown completo salvato su disco
- Un verdetto conversazionale breve (3-5 righe) da presentare all'utente

## Qualita del report
- Scrivi in italiano chiaro e diretto
- Usa dati concreti, non opinioni vaghe
- Se un dato manca, dillo esplicitamente ("dato non disponibile")
- Evidenzia i trade-off, non nascondere le debolezze del prodotto consigliato
- Il report deve essere utile sia per una lettura veloce (verdetto + tabella) che approfondita (sezioni dettagliate)
