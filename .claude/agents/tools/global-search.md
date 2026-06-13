# Ricerca globale — Playbook

## Obiettivo
Cercare il prodotto nel mondo intero, non solo in Italia/EU. Sempre calcolare il costo totale di consegna in Italia.

## Siti globali da cercare

### E-commerce internazionali
| Sito | Regione | Note |
|------|---------|------|
| amazon.com | USA | Spesso prezzi base piu bassi, ma dazi + spedizione |
| ebay.com | Globale | Venditori worldwide, controllare spedizione |
| aliexpress.com | Cina | Prezzi molto bassi, tempi lunghi, qualita variabile |
| banggood.com | Cina | Elettronica, magazzini EU disponibili |
| bhphotovideo.com | USA | Elettronica/foto, spedisce worldwide |
| japan-shopping / kakaku.com | Giappone | Per prodotti audio/foto di nicchia |

### E-commerce EU (oltre Italia)
| Sito | Paese | Note |
|------|-------|------|
| mediamarkt.de | Germania | Spesso prezzi migliori del MediaWorld italiano |
| saturn.de | Germania | Stessa catena di MediaMarkt |
| coolblue.nl / coolblue.de | NL/DE | Ottimo servizio, spedisce in EU |
| fnac.com | Francia | Elettronica + cultura |
| pccomponentes.com | Spagna | Ottimo per componenti PC |
| alternate.de | Germania | Componenti e periferiche |
| thomann.de | Germania | Audio/musica, spedisce worldwide |

## Calcolo costo totale verso Italia

### Da EU (no dazi)
```
Totale = Prezzo + Spedizione
```
Nessun dazio doganale, IVA gia inclusa nel prezzo.

### Da UK (post-Brexit)
```
Totale = Prezzo + Spedizione + IVA import (22%) + Gestione doganale corriere (~10-15€)
```
Soglia esenzione: ordini sotto 150€ di valore merce possono avere IVA pre-pagata dal venditore.

### Da USA / resto del mondo
```
Totale = Prezzo (convertito in EUR) + Spedizione internazionale + Dazio doganale (varia per categoria, tipicamente 0-6% per elettronica) + IVA import (22% su valore + spedizione + dazio) + Gestione doganale corriere (~10-15€)
```

### Da Cina (AliExpress, Banggood)
```
Totale = Prezzo + Spedizione (spesso gratuita ma lenta)
```
- Ordini sotto 150€: spesso IVA gia inclusa (IOSS)
- Ordini sopra 150€: dazio + IVA + gestione doganale
- Tempi: 15-45 giorni (standard), 7-15 giorni (magazzino EU)
- Banggood/AliExpress hanno magazzini EU — prioritizzare quelli

## Strategia di ricerca

1. **Prima cerca in EU** — nessun dazio, spedizione veloce
2. **Poi cerca globale** — solo se il risparmio supera i costi extra
3. **Calcola SEMPRE il totale** — prezzo + spedizione + dazi/IVA
4. **Segnala i tempi** — l'utente deve sapere se aspettera 3 giorni o 30
5. **Segnala i rischi** — garanzia EU non valida per acquisti extra-EU, assistenza piu complicata

## Conversione valute
- Usa il tasso di cambio corrente (cercalo con WebSearch: "EUR to USD exchange rate")
- Aggiungi 2-3% per commissione carta di credito su valute non-EUR
