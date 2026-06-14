# EPREL — Playbook di navigazione

## Come funziona
EPREL (European Product Registry for Energy Labelling) e il database ufficiale della Commissione Europea per le etichette energetiche. Contiene dati su tutti i prodotti con energy label venduti in EU: classe energetica, consumo annuo, scheda informativa (PIS), e etichetta in formato elettronico.

## Portale pubblico
- URL base: `https://eprel.ec.europa.eu/`
- Accesso: gratuito, nessuna registrazione necessaria per consultazione

## Strategia di ricerca

### 1. Trovare il prodotto su EPREL
WebSearch con query:
```
site:eprel.ec.europa.eu "[nome modello]"
```
oppure:
```
EPREL "[brand] [modello]" energy label site:ec.europa.eu
```

### 2. Ricerca per categoria
Le categorie EPREL rilevanti per il progetto buyer:

| Categoria EPREL | Prodotti |
|-----------------|----------|
| televisions | TV, monitor con tuner |
| electronic displays | Monitor senza tuner |
| refrigerating appliances | Frigoriferi, congelatori |
| washing machines | Lavatrici |
| washer-dryers | Lavasciuga |
| dishwashers | Lavastoviglie |
| air conditioners | Climatizzatori |
| light sources | Lampadine, LED |
| tyres | Pneumatici |

### 3. URL diretti per ricerca
```
https://eprel.ec.europa.eu/screen/product/televisions
```
Sostituire `televisions` con la categoria corretta.

### 4. Estrazione dati con WebFetch
Per ogni prodotto trovato su EPREL, estrarre:
- **Classe energetica** (A-G, scala 2021)
- **Consumo energetico** (kWh/1000h in SDR e HDR)
- **Dimensioni schermo** (diagonale in cm e pollici)
- **Risoluzione** (pixel orizzontali x verticali)
- **Scheda informativa prodotto (PIS)** — contiene dettagli tecnici completi
- **Codice QR** dell'etichetta energetica
- **Fornitore** e **identificativo modello** del produttore

### 5. Confronto classe energetica
La scala EU 2021 (rescaled) va da A a G:
- **A-B**: eccellente efficienza (raro nei TV, quasi nessun modello)
- **C-D**: buona efficienza (OLED premium, LED efficienti)
- **E-F**: media (maggior parte dei TV LCD/QLED)
- **G**: bassa efficienza (modelli grandi, alta luminosita)

Nota: la classe e calcolata su consumo SDR standard. In HDR il consumo e tipicamente 30-60% piu alto.

## Dati disponibili per il SustainabilityScout

EPREL fornisce dati oggettivi e verificabili per:
1. **Confronto efficienza energetica** tra modelli concorrenti
2. **Consumo annuo stimato** (basato su uso standard 1000h)
3. **Verifica claim produttore** — se il brand dichiara "classe energetica X", EPREL conferma o smentisce
4. **Carbon footprint indicativo** — il consumo energetico e il principale driver delle emissioni in fase d'uso

## Limitazioni
- Solo prodotti con obbligo di energy label EU (no accessori, no prodotti senza label)
- Dati inseriti dai produttori — EPREL non verifica indipendentemente (ma le autorita di sorveglianza del mercato possono)
- Non contiene dati su materiali riciclati, packaging, o emissioni di produzione
- Alcuni modelli recenti possono avere un ritardo di registrazione

## Note
- EPREL e la fonte piu autorevole per classe energetica — piu affidabile di schede prodotto dei retailer
- Il confronto consumo kWh/1000h e piu utile della classe energetica per il calcolo costi operativi
- I dati EPREL sono machine-readable e verificabili — ideale per cross-reference con claim dei produttori
