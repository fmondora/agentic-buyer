# eBay — Playbook di navigazione

## Domini da cercare

| Paese | Dominio | Note |
|-------|---------|------|
| Italia | ebay.it | Mercato primario |
| Germania | ebay.de | Grande catalogo, molti venditori pro |
| UK | ebay.co.uk | Attenzione dazi post-Brexit |
| USA | ebay.com | Solo se risparmio significativo |
| Francia | ebay.fr | Copertura media |

## Strategia di ricerca

### 1. Ricerca prodotto
WebSearch:
```
site:ebay.[tld] "[nome prodotto]" -usato -ricondizionato
```

Per includere usato/ricondizionato (utile per LifecycleAdvisor):
```
site:ebay.[tld] "[nome prodotto]"
```

### 2. Filtri importanti
- **Nuovo**: per confronto prezzi standard
- **Ricondizionato certificato**: spesso 20-40% in meno, con garanzia
- **Venditori professionali**: preferire per garanzia e reso
- **Spedizione gratuita**: filtrare quando possibile
- **Posizione venditore**: preferire EU per evitare dazi

### 3. Estrazione dati
Per ogni inserzione:
- Prezzo (asta vs compralo subito)
- Spedizione verso Italia (costo + tempi)
- Posizione venditore (paese)
- Feedback venditore (% positivi, numero vendite)
- Condizione (nuovo / ricondizionato / usato)

### 4. Calcolo prezzo totale
- Da eBay EU: Prezzo + Spedizione
- Da eBay UK/USA: applicare regole da global-search.md

## Note
- eBay Ricondizionato Certificato ha garanzia 2 anni
- Verificare sempre il feedback del venditore (>98% positivo, >1000 vendite)
- I venditori cinesi su eBay hanno gli stessi tempi di AliExpress
