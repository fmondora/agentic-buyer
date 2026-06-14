---
allowed-tools: Bash, Read, Write, Edit, Agent, WebFetch, WebSearch, AskUserQuestion
---

# /track — Price Tracker

Gestisci il tracciamento prezzi dei prodotti nella watchlist.

## Parsing input

Analizza `$ARGUMENTS`:

- **Nessun argomento o "check"**: controlla i prezzi di tutti i prodotti tracciati
- **"check <id>"**: controlla solo un prodotto specifico
- **"list"**: mostra la lista dei prodotti tracciati
- **"add <prodotto>"**: cerca il prodotto, trova URL idealo/trovaprezzi, e aggiungilo alla watchlist
- **"history <id>"**: mostra lo storico prezzi di un prodotto
- **"report"**: genera un report markdown con grafici ASCII di tutti i prodotti
- **"purchased"**: mostra la lista dei prodotti acquistati (da `tracker/purchased.json`)
- **"purchased add <prodotto>"**: aggiungi un prodotto alla lista acquisti
- **"safety"**: controlla Safety Gate/RAPEX per TUTTI i prodotti acquistati — cerca richiami e alert di sicurezza
- **"safety <id>"**: controlla Safety Gate solo per un prodotto acquistato specifico

## Esecuzione

### check / check <id>
Lancia lo script Python:
```
python3.12 /Users/fmondora/wip/personal/buyer/tracker/check_prices.py check [id]
```
Mostra i risultati all'utente in modo leggibile.

### list
```
python3.12 /Users/fmondora/wip/personal/buyer/tracker/check_prices.py list
```

### add <prodotto>
1. Cerca il prodotto su idealo.it e trovaprezzi.it usando WebSearch
2. Trova gli URL delle pagine di confronto prezzi
3. Chiedi all'utente il budget e la soglia di alert (o usa default ragionevoli)
4. Aggiungi al watchlist.json con il comando:
```
python3.12 /Users/fmondora/wip/personal/buyer/tracker/check_prices.py add <id> <name> <url> <budget> <alert>
```
5. Esegui subito un primo check per registrare il prezzo iniziale

### history <id>
```
python3.12 /Users/fmondora/wip/personal/buyer/tracker/check_prices.py history <id>
```

### report
1. Leggi tutti i file CSV in `tracker/history/`
2. Per ogni prodotto, mostra:
   - Prezzo attuale vs prezzo al momento dell'aggiunta
   - Trend (salendo/scendendo/stabile)
   - Distanza dal budget e dalla soglia alert
3. Genera un riepilogo con consigli: "compra ora" se sotto alert, "aspetta" se trend in discesa

### purchased
Leggi `tracker/purchased.json` e mostra la lista formattata:
- ID, nome, brand, modello, prezzo pagato, data acquisto
- Report associato (link)
- Note (feedback da chiedere, etc.)

### purchased add <prodotto>
1. Chiedi: brand, modello, prezzo pagato, data acquisto, categoria
2. Genera un ID slug (brand-modello)
3. Aggiungi a `tracker/purchased.json`
4. Esegui subito un check safety per il nuovo prodotto

### safety / safety <id>
Per ogni prodotto acquistato (o solo quello specificato):
1. Leggi `tracker/purchased.json`
2. Per ogni prodotto, cerca su Safety Gate/RAPEX:
   - WebSearch: `site:ec.europa.eu/safety-gate "[brand]" "[modello]" OR "[categoria]"`
   - WebSearch: `site:ec.europa.eu/safety-gate "[brand]" recall [anno_acquisto]-[anno_corrente]`
   - WebSearch: `"RAPEX" OR "safety gate" "[brand] [modello]" richiamo alert`
3. Se trova alert rilevanti:
   - Mostra: data alert, tipo difetto, gravita, misure adottate
   - Segnala con **ATTENZIONE** in rosso
   - Suggerisci azione (contattare produttore, verificare modello/lotto)
4. Se non trova alert: "Nessun richiamo trovato — prodotto OK"
5. Mostra sempre la data dell'ultimo controllo

## Note
- Lo script usa solo stdlib Python (urllib, csv, json) — zero dipendenze
- I prezzi vengono salvati in CSV per semplicita e portabilita
- `tracker/purchased.json` tiene traccia di tutti i prodotti acquistati
- Il check safety puo essere eseguito periodicamente per monitorare richiami post-acquisto
- Il cron giornaliero puo essere configurato con: `crontab -e` aggiungendo:
  `0 9 * * * /opt/homebrew/bin/python3.12 /Users/fmondora/wip/personal/buyer/tracker/check_prices.py check`
