# Amazon EU — Playbook di navigazione

## Domini da cercare

| Paese | Dominio | Valuta | Note |
|-------|---------|--------|------|
| Italia | amazon.it | EUR | Mercato primario |
| Germania | amazon.de | EUR | Spesso il piu economico in EU |
| Francia | amazon.fr | EUR | Buona disponibilita |
| Spagna | amazon.es | EUR | Prezzi spesso competitivi |
| Paesi Bassi | amazon.nl | EUR | Catalogo piu ridotto |
| Belgio | amazon.com.be | EUR | Catalogo ridotto |
| Polonia | amazon.pl | PLN | Convertire in EUR |
| Svezia | amazon.se | SEK | Convertire in EUR |
| UK | amazon.co.uk | GBP | Attenzione: dazi doganali post-Brexit, IVA import |

## Strategia di ricerca

### 1. Ricerca prodotto
Per ogni dominio, usa WebSearch con query:
```
site:amazon.[tld] "[nome prodotto]"
```

Oppure WebFetch diretto:
```
https://www.amazon.[tld]/s?k=[query+url+encoded]
```

### 2. Estrazione prezzo
Da ogni pagina prodotto, cerca:
- Prezzo principale (inclusa IVA)
- Prezzo "altri venditori" (spesso piu basso)
- Prezzo Warehouse Deals (usato/ricondizionato)
- Coupon applicabili (tag "Applica coupon XX%")

### 3. Spedizione verso Italia
Per ogni Amazon non-italiano, verifica:
- **Spedizione diretta in Italia**: cerca "Spedisce in Italy" o "Delivers to Italy"
- **Costo spedizione**: WebFetch la pagina prodotto, cerca il blocco spedizione
- **Tempi di consegna**: standard vs express
- **Venduto e spedito da Amazon**: solo questi spediscono facilmente cross-border
- **Marketplace seller**: spesso NON spedisce fuori dal paese

### 4. Calcolo prezzo totale
```
Prezzo totale = Prezzo prodotto + Spedizione verso Italia + Eventuale IVA aggiuntiva
```

Per UK: aggiungere stima dazi doganali (~20% + gestione corriere ~10-15€)

### 5. Pattern URL utili
- Pagina prodotto: `https://www.amazon.[tld]/dp/[ASIN]`
- Stesso ASIN funziona su tutti i domini Amazon EU
- Cerca prima l'ASIN su amazon.it, poi controlla lo stesso ASIN sugli altri domini

## Trucchi
- Lo stesso prodotto ha spesso ASIN identico su tutti gli Amazon EU
- amazon.de ha spesso i prezzi migliori per elettronica
- amazon.es e competitivo per prodotti di consumo
- Warehouse Deals (amazon.de/outlet) puo avere sconti 20-30%
- I coupon variano per paese — controlla ogni dominio
