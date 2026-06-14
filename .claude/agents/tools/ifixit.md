# iFixit — Playbook di navigazione

## Come funziona
iFixit e il piu grande database al mondo di guide di riparazione e teardown. Fornisce:
- **Teardown**: smontaggio completo del prodotto con foto e analisi costruttiva
- **Score riparabilita**: voto 0-10 basato su teardown reale (facilita smontaggio, disponibilita ricambi, design)
- **Guide di riparazione**: istruzioni passo-passo per riparazioni comuni (schermo, batteria, componenti)
- **Ricambi**: vendita diretta di ricambi e attrezzi per molte categorie

## URL e ricerca

### Teardown (analisi costruttiva)
WebSearch:
```
site:ifixit.com "[brand] [modello]" teardown
```

### Guide di riparazione
WebSearch:
```
site:ifixit.com "[brand] [modello]" repair guide
```

### Score riparabilita per categoria
WebSearch:
```
site:ifixit.com "[brand]" repairability score
```

### URL diretti
- Teardown: `https://www.ifixit.com/Teardown/[Brand]+[Modello]+Teardown/[id]`
- Guide: `https://www.ifixit.com/Guide`
- Wiki dispositivi: `https://www.ifixit.com/Wiki/[categoria]`

## Dati estraibili per il LifecycleAdvisor

1. **Score riparabilita** (0-10) — basato su teardown reale, non su dichiarazioni del produttore
2. **Facilita apertura**: viti standard vs proprietarie, clip vs colla, attrezzi necessari
3. **Componenti sostituibili**: quali pezzi si possono cambiare, quali sono saldati/incollati
4. **Disponibilita ricambi**: iFixit vende ricambi? Parti facilmente reperibili?
5. **Guide disponibili**: quante guide di riparazione esistono per quel prodotto?
6. **Foto interne**: mostrano la qualita costruttiva reale (dissipazione, cablaggio, materiali)

## Categorie coperte
- Smartphone (copertura eccellente)
- Laptop / MacBook (copertura eccellente)
- Tablet (buona copertura)
- Console gaming (buona copertura)
- TV: copertura limitata — teardown disponibili solo per modelli selezionati
- Elettrodomestici: copertura parziale (lavatrici, aspirapolveri)
- Cuffie / auricolari: copertura crescente

## Limitazioni
- Non tutti i prodotti hanno un teardown — copertura dipende dalla popolarita del prodotto
- I TV hanno meno copertura rispetto a smartphone/laptop
- Lo score non copre tutti i modelli — per modelli senza score, usare i teardown di modelli simili dello stesso brand come proxy
- L'API iFixit esiste ma non e mantenuta attivamente — preferire WebSearch + WebFetch

## Note
- Il teardown iFixit e la fonte piu affidabile per valutare la riparabilita REALE — supera le dichiarazioni del produttore
- Per i TV: cercare teardown di modelli dello stesso brand e anno per avere un'idea della filosofia costruttiva
- Le guide di riparazione sono un valore aggiunto per il report: indicano al consumatore COME riparare, non solo SE si puo
