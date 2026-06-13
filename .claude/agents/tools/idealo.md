# idealo — Playbook di navigazione

## Come funziona
idealo e un comparatore prezzi europeo. Ha versioni per piu paesi, utile per confronto cross-border.

## Domini disponibili

| Paese | Dominio | Note |
|-------|---------|------|
| Italia | idealo.it | Mercato primario |
| Germania | idealo.de | Catalogo piu ampio, spesso prezzi migliori |
| Francia | idealo.fr | Buona copertura |
| Spagna | idealo.es | Copertura media |
| UK | idealo.co.uk | Attenzione dazi post-Brexit |
| Austria | idealo.at | Prezzi simili a .de |

## Strategia di ricerca

### 1. Ricerca prodotto
WebSearch con query:
```
site:idealo.[tld] "[nome prodotto]"
```

Oppure WebFetch:
```
https://www.idealo.[tld]/mscat.html?q=[query+url+encoded]
```

### 2. Estrazione dati
Per ogni prodotto trovato:
- Prezzo minimo tra tutti i venditori
- Lista venditori con rispettivi prezzi
- Storico prezzo (idealo mostra il grafico — cerca "prezzo piu basso degli ultimi X mesi")
- Costo spedizione per venditore

### 3. Confronto cross-border
- Cerca lo stesso prodotto su idealo.de e idealo.it
- Spesso il prezzo tedesco e inferiore
- Verifica che il venditore tedesco spedisca in Italia
- Calcola prezzo totale con spedizione

### 4. Vantaggi idealo
- Storico prezzi: mostra se conviene aspettare
- Alert prezzo: segnala all'utente se il prezzo e vicino al minimo storico
- Confronto cross-border nativo
- Include anche offerte Amazon, MediaMarkt, etc.

## Note
- idealo.de e spesso la fonte migliore per elettronica in Europa
- Lo storico prezzi aiuta a capire se un'offerta e davvero buona
