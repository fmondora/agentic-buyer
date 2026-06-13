# LifecycleAdvisor — Learnings

## Fonti affidabili

### Supporto software / OS
- **avmagazine.it** — articoli specifici su anni di aggiornamento per brand (Samsung 7 anni Tizen, LG 5 anni webOS)
- **smartworld.it** — notizie aggiornate su politiche aggiornamento TV
- **ilovemytv.it** — confronto OS smart TV (Tizen vs webOS vs VIDAA vs Google TV), ottima fonte per longevità software
- **hdblog.it** — aggiornamenti VIDAA Hisense, articoli tecnici affidabili
- **afdigitale.it** — politiche supporto Samsung e Hisense, buona sintesi

### Prezzi nuovi (IT)
- **idealo.it** — prezzi aggiornati e affidabili, include storico prezzi. Cerca "[modello]" + idealo.it
- **trovaprezzi.it** — buona copertura, ma spesso restituisce 403 a WebFetch diretto; usare WebSearch con "trovaprezzi [modello]"
- **everyeye.it/tech** — articoli con prezzi e offerte aggiornati

### Indice riparabilità Francia
- **indicereparabilite.fr** — database ufficiale, accessibile via WebFetch ma lista paginata; cercare per brand
- **Samsung**: score medi 7.5-8.1/10 per QLED 55" (QE55Q60T: 7.5, QE55Q80A: 8.1)
- **lcd-compare.com** — lista TV con score >= 7, ma ordinata per dimensione; filtrare per 55"

### Trade-in / programmi ritiro
- **samsung.com/it/offer/trade-up/** — Trade Up Samsung: fino a 500€ sconto, ritiro RAEE qualsiasi marca
- **lg.com/it/offerte/trade-up/** — Trade Up LG: 100-300€ sconto su TV selezionati, valido fino a 31/12/2026

### Costi riparazione
- **pgcasa.it** — costi riparazione TV italiani affidabili
- Dati chiave: pannello 55" costa 350-530€ (spesso non conveniente), retroilluminazione 100-180€, scheda madre/alimentatore 25-65€

## Fonti problematiche

- **trovaprezzi.it** (WebFetch diretto) — restituisce 403; usare WebSearch per estrarre i prezzi
- **subito.it** (WebFetch diretto) — restituisce 400; non navigabile via WebFetch
- **ebay.it** (WebFetch con filtri venduto) — spesso mostra solo ricambi nei risultati filtrati, non TV interi
- **picclick.it** — restituisce 404
- **prontopro.it** — carica CSS/JS ma non il contenuto testuale, inutile via WebFetch
- **planetricambitv.it** — ECONNREFUSED
- **shoesoffclub.com** — ECONNREFUSED
- **stereoindex.com** — redirect a hifiratings.com (301), poi non tentato

## Pattern di ricerca efficaci

- Per prezzi attuali: `"[modello esatto]" prezzo Italia idealo euro 2025` → ottieni cifre da idealo.it
- Per supporto software: `"[brand] TV anni aggiornamenti garantiti [OS]"` → trova comunicati ufficiali
- Per indice riparabilità: `site:indicereparabilite.fr [brand]` o WebFetch su `indicereparabilite.fr/etiquette-produit/[brand]/`
- Per valori usato: WebSearch `"[modello] usato prezzo subito ebay"` + brand → estrai range da snippet
- Per costi riparazione: WebSearch `riparazione TV 55 pollici costo [tipo] prezzo Italia` + pgcasa.it

## Note per categoria

### TV 55 pollici fascia 300-600€ (analisi giugno 2026)

**Modelli principali nella fascia target:**
| Brand | Modello | Prezzo (IT, giugno 2026) | OS |
|-------|---------|--------------------------|-----|
| Samsung | QE55Q60D (2024) | ~490-550€ | Tizen |
| LG | 55QNED80A6A (2025) | ~430-465€ | webOS |
| Hisense | 55U6NQ (2024) | ~400-450€ | VIDAA |
| Hisense | 55U7NQ (2024) | ~600-810€ (sopra target) | VIDAA |
| TCL | 55C655 (2024) | ~390-410€ | Google TV |
| Philips | 55PUS8909 (2024) | ~550-630€ | Google TV / Titan OS |

**Supporto software garantito:**
- Samsung Tizen: **7 anni** (modelli 2024+, alcuni 2023) — migliore della categoria
- LG webOS Re:New: **5 anni / 4 aggiornamenti OS** (modelli 2022-2025)
- Hisense VIDAA: **fino a 8 anni** dichiarati (formulazione ambigua, "fino a" = non garantito)
- TCL Google TV: segue ciclo Google Android — circa 3-5 anni pratici, non dichiarati esplicitamente
- Philips: in transizione Google TV → Titan OS (2026); Titan OS promette **10 anni** ma solo su modelli 2026+

**Indice riparabilità francese (TV):**
- Dal gennaio 2025 sostituito dall'indice di durabilità per i televisori
- Samsung: score tipici 7.5-8.1/10 su QLED — tra i migliori del mercato
- LG, Hisense, TCL, Philips: dati difficili da estrarre; Samsung e Philips citati come brand sopra 7/10
- TCL e Hisense: score non pubblicamente noti, probabilmente 6-7/10

**Riparabilità pratica:**
- Pannello 55" rotto: costo sostituzione 350-530€ (quasi sempre non conveniente)
- Retroilluminazione LED: 100-180€ (conveniente se TV ancora supportato)
- Scheda madre/alimentatore: 25-65€ manodopera + ricambio (economico, conveniente)
- Ricambi Samsung: disponibili su ricambisamsung.it e eBay.it; LG, Hisense, TCL su servicetvcrende.it, sos-ricambi.it
- Disponibilità ricambi: Samsung garantisce 7 anni di ricambi per legge EU; gli altri brand meno certi

**Valore usato stimato (2-3 anni):**
- TV 55" fascia 400-600€ dopo 2-3 anni: deprezzamento ~40-55%
- Samsung QE55Q60C (2023) acquistato ~550€ → valore 2025 stimato: 220-300€
- Hisense 55U6N (2024) acquistato ~420€ → valore 2027 stimato: 150-220€
- TCL 55C655 (2024) acquistato ~400€ → valore 2027 stimato: 130-200€
- Brand premium (Samsung, LG) tengono meglio il valore rispetto a brand cinesi (Hisense, TCL)

**Trade-in:**
- Samsung Trade Up: ritira qualsiasi TV RAEE, sconto fino a 500€ sul nuovo (flat, non basato sul modello vecchio)
- LG Trade Up: 100-300€ sconto su TV selezionati LG, valido fino a 31/12/2026
- Philips, TCL, Hisense: nessun programma trade-in ufficiale in Italia

### TV 55 pollici fascia 400-1000€ QLED puro e Mini-LED mid-range (analisi giugno 2026)

**Modelli principali nella fascia target (budget max 1000€):**
| Brand | Modello | Anno | Tecnologia | Prezzo (IT, giugno 2026) | OS |
|-------|---------|------|------------|--------------------------|-----|
| Samsung | QE55Q60D | 2024 | QLED | ~490–700€ | Tizen |
| Samsung | QE55Q70D | 2024 | QLED | ~548–680€ | Tizen |
| Samsung | QE55Q80D | 2024 | QLED (VA Full Array) | ~649–753€ | Tizen |
| TCL | 55C645 | 2023 | QLED | ~390–430€ | Google TV |
| TCL | 55C745 | 2023 | QLED | ~720€ | Google TV |
| TCL | 55C655 | 2024 | QLED | ~400€ | Google TV |
| Hisense | 55E7Q PRO | 2025 | QLED | ~395–450€ | VIDAA |
| Hisense | 55U7KQ | 2023 | Mini-LED ULED | ~508–520€ | VIDAA |
| Hisense | 55U8KQ/U8Q | 2023/2025 | Mini-LED ULED | ~746€ | VIDAA |

**Nota naming modelli:**
- Il modello "55C755" non risulta disponibile in Italia come sku dedicato; la serie C755 esiste solo in alcuni mercati. In Italia la fascia equivalente è il C745 o il C7L (~736€)
- L'E7K è la denominazione del modello 2023; nel 2025 si chiama E7Q PRO (stesso posizionamento)
- L'U7K è il modello 2023 della serie Mini-LED entry; nel 2024-2025 si chiama U7NQ/U7KQ

**Riparabilità specifica QLED mid-range:**
- Samsung Q60D/Q70D/Q80D: ricambi disponibili esclusivamente tramite centri assistenza autorizzati (Samsung non vende ai privati). Indice FR tipico ~7.5-8.1/10 (dati dalle generazioni T/A/B/D confermano continuità). Score relativamente alto grazie a documentazione tecnica disponibile e ricambi garantiti 7 anni per legge EU.
- TCL C645/C745: centri assistenza autorizzati in Italia (centriassistenza.org), ricambi originali disponibili, sito tcl.com/it con "Richiesta di riparazione". Indice FR/EU non pubblicato ufficialmente; stimato ~6-7/10 per analogia con brand cinesi simili.
- Hisense E7K/U7K/U8K: assistenza disponibile, indice non pubblico; stimato ~6-7/10.
- Costi riparazione aggiornati: pannello 55" LCD/QLED ~100-300€ (spesso non conveniente rispetto al valore TV); retroilluminazione LED ~100-180€; scheda madre/alimentatore ~100-250€.

**Valore usato stimato per fascia QLED 400-750€ (dopo 2-3 anni):**
- Samsung QE55Q60D (acquistato ~500€) → valore 2027: ~200-280€ (deprezzamento 44-60%)
- Samsung QE55Q70D (acquistato ~600€) → valore 2027: ~240-340€ (deprezzamento 43-60%)
- Samsung QE55Q80D (acquistato ~700€) → valore 2027: ~280-390€ (deprezzamento 44-60%)
- TCL 55C645 (acquistato ~400€) → valore 2026/2027: ~130-190€ (deprezzamento 52-67%)
- TCL 55C745 (acquistato ~720€) → valore 2026/2027: ~230-310€ (deprezzamento 57-68%)
- Hisense 55E7Q PRO (acquistato ~420€) → valore 2027: ~140-200€ (deprezzamento 52-67%)
- Hisense 55U7KQ (acquistato ~520€) → valore 2027: ~180-260€ (deprezzamento 50-65%)
- Hisense 55U8KQ (acquistato ~750€) → valore 2027: ~270-380€ (deprezzamento 49-64%)
- Samsung QLED mantiene valore residuo superiore in % rispetto a TCL e Hisense (~10-15% in più)

**Trade-in:**
- Samsung Trade Up: ritira qualsiasi TV RAEE, sconto flat (indipendente dal valore dell'usato) fino a ~500€; dettaglio sconto per modello non pubblicato online, dipende dal modello acquistato
- TCL: nessun programma trade-in ufficiale in Italia
- Hisense: nessun programma trade-in ufficiale in Italia

**Upgradabilità TV (categoria)**
- Tutti i TV di questa categoria hanno upgradabilità nulla a livello hardware (nessun componente espandibile dall'utente)
- Samsung: One Connect Box su Q80D e superiori (separa i connettori dal TV, riduce obsolescenza hardware); Q60D/Q70D non ce l'hanno
- TCL/Hisense: nessun sistema equivalente; standard HDMI 2.1 su modelli mid-high garantisce compatibilità futura con console/PC per 5-7 anni

**Longevità pannello QLED vs Mini-LED:**
- QLED puro (Q60D/Q70D/Q80D, C645/C745, E7Q): backlight edge LED o full array classico; nessun rischio burn-in, durata stimata pannello 50.000-80.000 ore
- Mini-LED ULED (U7K/U8K): backlight Mini-LED con local dimming avanzato; stesse considerazioni QLED, nessun rischio burn-in, durata analoga

### TV 55 pollici fascia 600-1000€ OLED e Mini-LED premium (analisi giugno 2026)

**Modelli principali nella fascia target:**
| Brand | Modello | Anno | Tecnologia | Prezzo (IT, giugno 2026) | OS |
|-------|---------|------|------------|--------------------------|-----|
| LG | OLED55C45LA | 2024 | OLED evo (W-OLED) | ~725€ | webOS |
| LG | OLED55C55LA | 2025 | OLED evo (W-OLED) | ~634€ | webOS |
| Samsung | QE55S90D | 2024 | QD-OLED | ~969€ (al limite del budget) | Tizen |
| Samsung | QE55S90F / S90FAE | 2025 | QD-OLED | ~684-870€ | Tizen |
| Samsung | QE55QN85F | 2025 | Neo QLED Mini-LED | ~699-718€ | Tizen |
| Hisense | 55U8Q | 2025 | Mini-LED ULED | ~746€ | VIDAA |
| TCL | 55C805 | 2023 | QD-Mini LED | ~472-799€ (saldo) | Google TV |

**Supporto software garantito (fascia premium):**
- Samsung OLED (S90D/F): **7 anni Tizen** — stessa politica QLED, confermata 2024+
- LG OLED C-series webOS Re:New: **5 anni / 4 aggiornamenti OS**
  - C4 (2024): aggiornato fino a webOS 28 (2029)
  - C5 (2025): aggiornato fino a webOS 29 (2030)
- Hisense U8 VIDAA: "fino a 8 anni" dichiarati (ambiguo)
- TCL C805 Google TV: ~3-5 anni pratici

**Burn-in OLED — stato del rischio (2025-2026):**
- Rischio concreto ma molto ridotto rispetto a 5 anni fa (tecnologie di mitigazione: pixel shift, ABL, logomasking)
- W-OLED LG: pannello WOLED più robusto contro burn-in rispetto ai predecessori OLED RGB
- QD-OLED Samsung (S90): maggiore luminosità di picco (1500-2000 nit), ma più soggetto a burn-in su contenuti statici ripetuti (canali sportivi con score fisso, news ticker)
- Stima durabilità a uso misto (5h/die): 30.000+ ore a metà luminosità = 16+ anni
- Rischio concreto solo per: uso >8h/die, canali TV lineari con logo fisso, gaming con HUD statico senza screen saver
- Consiglio pratico: tenere OLED Light su <50 su LG, attivare energy saving su Samsung; mai lasciare immagine statica >2 minuti

**Valore usato stimato (modelli 2-3 anni fa, dati giugno 2026):**
- LG OLED C2 55" (acquistato 2022 ~1400€) → valore attuale: ~400-600€ (deprezzamento 55-70%)
- LG OLED C3 55" (acquistato 2023 ~1200€) → valore attuale: ~550-750€ (deprezzamento 35-55%)
- Samsung S90D 55" (acquistato 2024 ~1000€) → valore stimato 2027: ~450-600€
- Samsung QN85F 55" (acquistato 2025 ~720€) → valore stimato 2028: ~300-400€
- OLED deprezza meno in % rispetto a LCD/QLED grazie alla domanda elevata di usato, ma il valore assoluto parte più alto
- LG OLED C-series mantiene il valore meglio di qualsiasi altro brand TV sul mercato usato italiano

**Note tecnologia a confronto (OLED vs Mini-LED):**
- OLED: nero perfetto, angoli visione eccellenti, nessun blooming, ma burn-in teorico e luminosità assoluta inferiore a Mini-LED
- Mini-LED (Neo QLED / U8 / C805): luminosità di picco superiore (1000-2000 nit), ottimo per ambienti luminosi, ma blooming residuo ai bordi delle zone
- Per uso misto (film + gaming + TV generalista): OLED vince su qualità immagine e longevità del pannello se usato correttamente
- Per salotti molto luminosi o uso >8h/die: Mini-LED più sicuro
