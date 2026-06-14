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

### Ombrelloni da esterno palo laterale/sbalzo (analisi giugno 2026)

**GAP CRITICO DI BUDGET**: I brand nominati nel discovery (Scolaro, Caravita, FIM, Umbrosa, Doppler) sono tutti prodotti professionali/semi-professionali con prezzi reali 1.000-2.500€+. Il budget 500-700€ non copre nessuno di questi brand per dimensioni 3.5m+. Il Scolaro Napoli Braccio Ø3.5 costa ~1.060€ IVA inclusa (già scontato del 40%). Informare sempre l'utente di questo gap.

**Modelli e prezzi accertati (giugno 2026):**
| Brand | Modello | Dimensione | Prezzo (IVA inclusa) | Note |
|-------|---------|------------|---------------------|------|
| Scolaro | Napoli Braccio | Ø3.5m | ~1.060€ (scontato da ~1.766€) | Entry-level Scolaro |
| Scolaro | Palladio Braccio | 3.5x3.5m | ~1.650€ (scontato da ~2.750€) | Struttura alluminio+legno Iroko |
| Scolaro | Leonardo Braccio | 3.5x3.5m | ~1.796€ (scontato da ~2.513€) | Professionale, 70kg |
| FIM | Capri | 3.5x3.5m | ~1.433€ | Made in Italy |
| Umbrosa | Paraflex | Ø2.7-3m | fuori produzione su alcuni canali | Alluminio, garanzia 15 anni profili |

**Garanzie accertate:**
- Scolaro: 2 anni struttura, 1 anno meccanismo, 5 anni telo (Teflon/Dralon 350gr/m²)
- Umbrosa: 15 anni profili alluminio, 5 anni nervature + acciaio inox, 5 anni telo contro scolorimento, 3 anni plastica, 2 anni basi
- FIM: non dichiarata pubblicamente sul sito prodotto (contattare rivenditore)
- Caravita: PDF garanzia disponibile su richiesta; ricambi per "quasi ogni componente" confermati
- Doppler: 3 anni garanzia dichiarata

**Ricambi e riparabilità:**
- Scolaro: stecche intercambiabili senza smontare la struttura (sistema brevettato); teli sostitutivi disponibili su citsshop.it, levanteshop.it, greenterest.it
- FIM: teli sostitutivi disponibili su greenterest.it (es. telo 3x4m disponibile), ricambi da rivenditori autorizzati
- Caravita: sostituzione telo in 6 passi (svitare pomello, aprire a metà, allentare viti bracci, rimuovere telo) — fai-da-te possibile
- Glatz: ricambi tramite rete rivenditori, telo sostitutivo disponibile "se il modello è ancora in gamma"; no deposito ricambi centrale
- Umbrosa: ricambi dettagliati nei manuali di installazione, zip di ricambio spedibili direttamente

**Prezzi teli sostitutivi (range accertato):**
- Telo FIM 3x4m: ~80-120€ (greenterest.it)
- Telo generico 4x3m palo laterale: ~49.90€ (grupposanmarco.eu)
- Telo Scolaro Napoli/Leonardo (telo originale): prezzo non trovato online, tramite rivenditore autorizzato

**Uso montagna — considerazioni specifiche:**
- Ombrelloni palo laterale NON adatti a posizioni molto esposte al vento (raccomandazione comune tra produttori)
- Per uso montagna: preferire strutture con profilo palo >70x70mm, stecche in alluminio 18x30mm+
- Scolaro Leonardo: palo 92x92mm — il più robusto della gamma entry-semi-pro
- Indispensabile base cementata o contrappesi adeguati (2-6 unità per ø3.5m)
- Chiudere sempre l'ombrellone in caso di vento, pioggia forte, grandine

**Indice riparabilità francese:** Non applicabile a ombrelloni (categoria non coperta da indice obbligatorio).
**iFixit:** Non copre ombrelloni (categoria non presente).

**Fonti affidabili per ombrelloni:**
- greenterest.it — rivenditore FIM autorizzato, ha teli di ricambio e guida acquisto ricambi
- caffegrazie.it — rivenditore Scolaro, prezzi aggiornati e scontati
- designperte.it — prezzi Scolaro aggiornati con dettagli tecnici
- umbrosashop.com — garanzia Umbrosa dettagliata, ricambi
- caravita.eu — FAQ ricambi e istruzioni sostituzione telo

**Fonti problematiche per ombrelloni:**
- dopplershop.it — pagina JS-heavy, WebFetch non restituisce contenuto prodotti
- bsvillage.com Umbrosa Paraflex — articolo fuori produzione
- caravita.eu/warranty/ — PDF esterno non accessibile, informazioni garanzia non nel HTML

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

### TV 55 pollici fascia 1000-5000€ OLED/QD-OLED premium (analisi giugno 2026)

**Modelli principali nella fascia target:**
| Brand | Modello | Anno | Tecnologia | Prezzo (IT, giugno 2026) | OS |
|-------|---------|------|------------|--------------------------|-----|
| Samsung | QE55S95D | 2024 | QD-OLED | ~1.299€ (listino 1.999€) | Tizen |
| Samsung | QE55S95F | 2025 | QD-OLED | ~1.085-1.354€ | Tizen |
| LG | OLED55G45LW / G46LS | 2024 | WOLED evo MLA | ~1.297€ | webOS |
| LG | OLED55G54LW / G56LS | 2025 | WOLED evo MLA+ (4-layer) | ~989-1.499€ | webOS |
| Sony | XR-55A95L | 2023 | QD-OLED | ~2.599€ | Google TV |
| Sony | XR-55A95M (BRAVIA 9) | 2024 | QD-OLED | ~2.500-3.000€ stimato | Google TV |
| Philips | 55OLED+909 | 2024 | WOLED | ~2.945€ (idealo) | Google TV |
| Philips | 55OLED+910 | 2025 | WOLED | ~2.290€ | Titan OS |
| Panasonic | TX-55MZ2000 | 2023 | WOLED MLA | ~1.760-2.895€ | MyHomeScreen 8 |
| Loewe | bild i.55 DR+ | 2024 | WOLED | ~2.100-2.500€ stimato | os7 (proprietario) |

**Nota modelli disponibilità:**
- Il "BRAVIA 9" non esiste come modello autonomo in Italia nel 55": Sony usa la sigla XR-55A95M o XR-55A95L. Il BRAVIA 9 è il nome commerciale della gamma 2024 (LCD Mini-LED, non OLED) — per OLED QD la serie rimane A95x
- Panasonic MZ2000 è il 2023; dal 2024 Panasonic è passata a Fire TV OS (serie Z95A/Z93A); l'MZ2000 usa MyHomeScreen 8 e non riceverà aggiornamenti OS significativi
- Loewe bild i: OS proprietario "os7" — dipendente dal vendor per aggiornamenti, rete distributiva limitata in Italia

**Supporto software garantito (fascia premium OLED):**
- Samsung S95D (2024) / S95F (2025): **7 anni Tizen** — confermato dalla politica Samsung per modelli 2024+; S95D garantito fino a 2031, S95F fino a 2032. Aggiornamento a Tizen OS 9 confermato giugno 2026
- LG G4 (2024): webOS Re:New — **5 anni / 4 aggiornamenti OS** — riceverà webOS 25/26/27/28, supporto fino a 2029
- LG G5 (2025): webOS Re:New — **5 anni / 4 aggiornamenti OS** — supporto fino a 2030
- Sony A95L (2023) / A95M (2024): Google TV — **non dichiarato ufficialmente** — Sony non ha una politica pubblica di anni garantiti; prassi storica: 4-6 anni di patch, OS major non garantiti; rischio medio-alto di obsolescenza software anticipata
- Philips OLED+909 (2024): Google TV — stessa situazione Sony; Philips in transizione verso Titan OS, i modelli 2024 Google TV non hanno garanzia esplicita
- Philips OLED+910 (2025): **Titan OS — 10 anni dichiarati** (da TP Vision) ma è il primo anno della piattaforma, verifica track record impossibile
- Panasonic MZ2000 (2023): MyHomeScreen 8 — OS abbandonato da Panasonic nel 2024; **nessun aggiornamento OS futuro garantito**. Solo patch di sicurezza sporadiche. Scelta a rischio sul lungo termine
- Loewe bild i: os7 proprietario — **totalmente dipendente da Loewe**; l'azienda ha avuto problemi di insolvenza in passato (2018-2019, rilevata da SKYTEC); roadmap aggiornamenti non pubblica. Rischio molto elevato di abbandono software

**Burn-in OLED — dati reali 2026 (test Rtings 50.000+ ore):**
- Cinema/home theater (uso tipico): **rischio concreto vicino a zero** — test Rtings su LG C2/C3/C4: zero casi confermati di burn-in da uso normale in 3 anni di tracking
- Scenari ad alto rischio: canali news 20h/die → burn-in visibile dopo ~4.000h (6 mesi); display digitale commerciale; gaming con HUD statico 8+h/die per mesi
- **QD-OLED vs WOLED — parity 2025-2026**: Samsung afferma che i pixel blu QD-OLED aging più rapidamente, ma test indipendenti non confermano differenza pratica per uso domestico. WOLED ha track record più lungo (dal 2013), QD-OLED dal 2022 quindi dati 4 anni disponibili. Entrambi sicuri per uso misto
- Differenza principale QD-OLED/WOLED: QD-OLED (S95D/F, A95L) più luminoso in picco (2000-2500 nit), migliore per ambienti luminosi. WOLED (LG G4/G5, Philips) più uniforme, meno stress per il pannello a luminosità moderate
- Mitigazione integrata 2025: pixel shift (default on), Automatic Brightness Limiter, Panel Compensation Mode (si attiva in standby). Nessuna azione speciale richiesta per uso cinema

**Riparabilità OLED premium:**
- Pannello OLED 55" danneggiato: sostituzione costa tipicamente 800-1.400€ (quasi sempre non conveniente rispetto al valore TV usato)
- Samsung S95D/F: assistenza tramite centri Samsung autorizzati; ricambi garantiti 7 anni per legge EU; pannello QD-OLED prodotto da Samsung Display, filiera interna
- LG G4/G5: assistenza LG autorizzata; pannello WOLED prodotto da LG Display, filiera interna; rete assistenza capillare in Italia
- Sony A95L: pannello QD-OLED Samsung Display; assistenza Sony autorizzata; costi manodopera elevati (brand premium); rete assistenza presente in Italia
- Philips OLED+909/910: pannello WOLED LG Display; assistenza TP Vision/Philips; rete assistenza meno capillare rispetto a Samsung/LG
- Panasonic MZ2000: pannello WOLED MLA LG Display; assistenza Panasonic in Italia (support-it.panasonic.eu); centri autorizzati presenti
- Loewe bild i: pannello WOLED; assistenza solo tramite rivenditori autorizzati Loewe (rete molto limitata in Italia ~20 punti vendita); **ricambi a rischio a lungo termine**
- Indice riparabilità francese/EU: per TV OLED premium non pubblicato individualmente; Samsung tipicamente 7.5-8.1/10 per i modelli QLED/OLED, altri brand non verificabili

**Valore usato stimato (OLED premium 55", dopo 2-3 anni):**
- LG OLED G-series: deprezza bene il primo anno (~25-35%), poi stabilizza. G3 55" (acquistato 2023 ~2.000€) → valore 2026 stimato: 700-1.000€
- LG G4 55" (acquistato 2024 ~1.800-2.200€) → valore 2027 stimato: 650-1.000€
- Samsung S95D 55" (acquistato 2024 ~2.000€, ora ~1.299€ nuovo) → valore usato attuale: ~700-1.000€; deprezza più rapidamente quando il nuovo scende di prezzo
- Samsung S95F 55" (acquistato 2025 ~1.400€) → valore 2028 stimato: 500-750€
- Sony A95L 55" (acquistato 2023 ~3.300€, ora ~2.599€) → valore usato stimato: 1.200-1.700€ (tiene bene perché partiva alto)
- Philips OLED+909 55" (~2.900€ nuovo) → valore usato 2-3 anni: 900-1.300€ (domanda usato Philips OLED moderata)
- Panasonic MZ2000 55" (~2.895€ nuovo) → valore usato attuale (2026, 3 anni): 700-1.100€
- Loewe bild i 55" → mercato usato molto ristretto in Italia; valore difficile da stimare; liquidità bassa

**Trade-in (giugno 2026):**
- Samsung Trade Up: ritiro qualsiasi TV RAEE + sconto sul nuovo (sconto dipende dal modello scelto; per S95F/S95D: stimato 200-500€ flat)
- LG Trade Up: sconto a carrello fino a **3.000€** (promozione lancio gamma 2026 valida fino a 10/06/2026, poi ridiventa sconto standard ~300-1.000€ sui G-series); ritiro 1-per-1 qualsiasi marca
- Sony: nessun programma trade-in strutturato in Italia; ritiro RAEE solo tramite rivenditori
- Philips: nessun programma trade-in in Italia
- Panasonic: nessun programma trade-in in Italia
- Loewe: nessun programma trade-in in Italia

**Fonti confermate per questa categoria:**
- idealo.it: prezzi attuali verificati per S95F (da €1.085), LG G5 (da €989), Sony A95L (€2.599), Philips OLED909 (€2.945)
- afdigitale.it: prezzi italiani Philips OLED+910 confermati (55": €2.290), LG trade-up dettagli promozione 2026
- cinemaconfig.com/blog/oled-burn-in-2026-real-data: dati burn-in affidabili, basati su test Rtings 50.000h
- whathifi.com: politica 7 anni Samsung TV
- avmagazine.it: webOS Re:New LG confermato 5 anni
- lgnewsroom.it: LG trade-up 2026 fino a 3.000€ conferma promozione
- flatpanelshd.com: transizione Panasonic a Fire TV OS, abbandono MyHomeScreen
