# ReviewAnalyst — Learnings

## Fonti affidabili

- **Altroconsumo** — test indipendenti con voto /100, pro/contro strutturati, molto affidabile per TV. URL pattern: `altroconsumo.it/hi-tech/televisori/comparatore/[modello]/[id]`
- **Tuttoandroid.net** — recensioni italiane dettagliate con voto /10, tono editoriale, buon accesso via WebFetch
- **QualeScegliere.it** — recensioni con voto /10 e pro/contro, accessibile via WebFetch (es. Sony Bravia 5 55, Sony X85L 55)
- **MenteInformatica.it** — guide all'acquisto con prezzi e confronti aggiornati, buon accesso
- **WebSearch generale** — query in italiano con "[modello] recensione italia voto pro contro" restituisce sintesi multi-fonte utili
- **Trovaprezzi.it** — prezzi aggiornati e opinioni utenti; anche contenuti editoriali utili (es. confronti U8N vs U8Q)
- **Leroy Merlin IT** — recensioni utenti con stelle (es. 4.5/5 su 178 rec per TCL C655)
- **PcComponentes.it** — recensioni utenti con stelle, ma restituisce 403 via WebFetch diretto
- **Everyeye.it / tech.everyeye.it** — recensioni italiane approfondite, buon accesso via WebSearch snippet
- **Multiplayer.it** — recensioni italiane dettagliate (es. TCL C80), snippet utili via WebSearch
- **HDblog.it** — recensioni italiane con dettagli tecnici (es. LG QNED86, Hisense U8Q)
- **AVForums.com** — recensioni internazionali professionali dettagliate, buon accesso via WebSearch snippet (es. Samsung QN85D)
- **WhatHiFi.com** — recensioni internazionali con focus audio/video, snippet utili (es. Samsung Q80D, QN90F)
- **TechRadar** — recensioni internazionali, snippet utili via WebSearch (es. Samsung Q80D, QN90F)
- **Idealo.it** — prezzi aggiornati con storico; molto affidabile per verificare disponibilità e range prezzo

## Fonti problematiche

- **RTings.com** — la pagina restituisce solo JS/codice, nessun testo utile via WebFetch
- **Amazon.it** — restituisce pagina CAPTCHA/verifica, non accessibile via WebFetch
- **PcComponentes.it** — 403 Forbidden su WebFetch diretto
- **Multiplayer.it / HDblog.it** — a volte 429 (rate limit) su WebFetch; ritentare dopo pausa
- **Altroconsumo comparatore** — la pagina hub non mostra i singoli prodotti, usare URL diretto del prodotto specifico

## Pattern di ricerca efficaci

- `"[modello] recensione italia [anno] voto pro contro"` — restituisce sintesi multi-fonte nella risposta WebSearch
- `"[modello] amazon.it recensioni stelle problemi"` — per opinioni utenti e criticità reali
- `"Altroconsumo [modello]"` + URL diretto per test indipendenti
- Per prezzi aggiornati: `trovaprezzi.it` o `idealo.it`
- Per confronti rapidi brand: `"Hisense vs TCL" site:rtings.com` o `site:whathifi.com`
- Per fascia 700-1000€: aggiungere "everyeye" o "avforums" alla query per trovare recensioni più approfondite
- Per verificare disponibilità taglio 55": specificare sempre "55 pollici [modello] prezzo italia euro" — alcuni modelli premium (es. TCL C855) esistono solo da 65" in su

## Lezioni operative

- **Budget chiamate**: max 20 WebSearch + 8 WebFetch. Se un prodotto non ha recensioni dopo 3 query, segnare "Recensioni insufficienti" e andare avanti. Mai riformulare la stessa query piu di 2 volte.
- **Prodotti di nicchia (outdoor, HORECA, professionali)**: le fonti tech (RTings, WhatHiFi, Tom's Hardware) NON hanno nulla. Usare: Amazon multi-EU, YouTube, forum di settore, Trustpilot brand, Reddit r/BuyItForLife.
- **Brand professionali italiani** (es. Scolaro, FIM, Danieli): quasi zero recensioni online. Proxy utili: longevita di mercato (anni di attivita), presenza HORECA (bar/ristoranti), feedback su subito.it (usato).
- **Ombrelloni/giardino**: fonti utili sono Amazon.it/de recensioni (via WebSearch, non WebFetch), ManoMano.it, Leroy Merlin recensioni, YouTube "test ombrellone vento".

## Note per categoria

### Legno/tavole per rivestimento parete (aggiornato giugno 2026)

#### Venditori italiani online — punteggi Trustpilot/TrustedShops
- **legnonline.it**: 5/5 su Trustpilot, ~2.944 recensioni — leader assoluto, imballaggio eccellente, tagli precisi. Primo classificato categoria "fornitore di legname" su TP
- **regnodellegno.com**: 4.63/5 su TrustedShops, 859 recensioni — imballaggio su pallet robusto, corriere BRT problematico
- **bricolegnostore.it**: 4/5 su Trustpilot, ~660-792 recensioni — qualità ok, imballaggio citato come buono, isolati casi listelli rotti per nodi
- **apropositodilegno.it**: 4.6/5 su Trustpilot, 71 recensioni — alta variabilità esperienze (75% cinque stelle ma 16% una stella), ritardi consegna segnalati
- **regnodellegno.it (TrustedShops)**: distinto da .com, solo 4 pagine recensioni — non confondere i due domini
- **legnopregio.com**: ~82 recensioni Trustpilot, feedback positivi su imballaggio e servizio clienti
- **tagliolegno.it**: 4.4/5 Trustpilot, solo 12 recensioni — troppo poche per essere affidabile

#### Criticità strutturali categoria legno spedito online
- **Lunghezza 200cm**: limite critico per i corrieri standard. Sopra i 150cm si richiede in genere spedizione su pallet/bancale (2-3 gg lavorativi invece di 1-2)
- **Imbarco**: problema quasi universale su legno grezzo non stagionato. Spessore 18mm particolarmente sensibile
- **Umidità**: legno in stock a umidità ~18% (dichiarata da venditori come Gartenwelt). A 18mm, un delta umidità del 5% causa variazioni dimensionali visibili
- **Nodi**: la categoria "larice" ha tipicamente nodi. Specificare sempre la classe qualitativa: "A/B senza nodi", "B/C con nodi", "rustico"
- **Resi su legname**: nessun venditore italiano accetta resi per "nodi naturali" o "variazioni di colore" — sono caratteristiche del legno, non difetti. I resi vengono accettati solo per danni da trasporto (con foto) o errore di misura

#### Offerta prodotti — formato rivestimento parete 80x200cm
- **Formato 80x200x18mm NON esiste come prodotto standard** su nessuna delle piattaforme analizzate
- Le piattaforme vendono: larghezze 100-190mm, lunghezze 140-400cm, spessori 18-52mm
- Per avvicinarsi al target: cercano tavole ~100-120mm x 200cm x 20-27mm (poi eventuale taglio su misura)
- Nordholz.it: pannelli 1970x196x19mm a 74€/pezzo — piu vicini alla specifica ma larghezza 196mm (non 80mm)
- Gartenwelt Riegelsberger (Amazon.it): arriva fino a 190cm, non 200cm. Larghezze 95-190mm

#### Fonti problematiche per questa categoria
- **Trustpilot WebFetch**: sempre 403 Forbidden — usare solo snippet da WebSearch
- **Amazon.it WebFetch**: CAPTCHA — usare WebSearch con "amazon.it [prodotto] recensioni"
- **ManoMano WebFetch**: 403 Forbidden — usare WebSearch per trovare prodotti
- **Reddit IT**: nessun thread trovato su acquisto legno online Italia — comunita troppo piccola per questo nicho
- **TrustedShops WebFetch**: accessibile e utile (regnodellegno.com trovato con dati dettagliati)

#### Pattern di ricerca efficaci per legno online
- `"[venditore].it" recensioni trustpilot imballaggio spedizione qualità legno` — recupera snippet con voto e temi
- `trustpilot "[venditore]" legno` — snippet Trustpilot accessibili via WebSearch
- `trustedshops.it/valutazione-del-negozio/[slug-venditore]` — WebFetch funziona, dati strutturati con recensioni testuali
- Per trovare venditori: `larice 200cm rivestimento parete acquisto online shop italy` — restituisce negozi specializzati



### Ombrelloni da esterno (aggiornato giugno 2026)
- Brand professionali (Scolaro, FIM, Caravita, Umbrosa) hanno quasi zero recensioni consumer online — sono venduti B2B
- Le recensioni utili sono su Amazon per i modelli consumer/mid-range (Doppler, tectake, IDMarket)
- YouTube ha video test vento per ombrelloni generici ma raramente per brand specifici
- Il proxy migliore per qualita e la presenza nelle terrazze HORECA (alberghi, ristoranti)
- **testbericht.de**: 403 Forbidden su WebFetch — inutilizzabile; snippets da WebSearch utili invece
- **galaxus.de/at**: timeout 60s su WebFetch — inutilizzabile
- **Doppler Active 370**: voto 4.6/5 su testbericht.de (snippet), venditore austriaco ~569€ AT vs ~799€ IT (differenza reale +40%). Criticita note: telo poliestere piu sottile dell'acrilico, meccanismo inclinazione che si inceppa su GS Active, base richiede 140-200kg per stare ferma con vento
- **Scolaro Napoli Braccio**: palo 75x75mm alluminio+acciaio, tela acrilica 350g/m2, sistema "Easy Change" per teli, inclinazione 20°, 360°. Uso professionale confermato (bar/hotel). Zero recensioni consumer trovate
- **Scolaro Palladio Braccio**: palo 92x92mm alluminio finitura legno, stecche in legno vero (iroko), peso 75-80kg. Piu robusto del Napoli. Zero recensioni consumer trovate
- **FIM Rodi**: stecche sostituibili singolarmente senza smontare (vantaggio HORECA), viteria inox, alluminio. Prezzo da ~1.690€. Zero recensioni consumer trovate
- **PiscineOnline**: zero recensioni sulla pagina prodotto — prodotto troppo recente o vendita bassa
- **greenterest.it**: rivenditore FIM con guida ricambi utile per capire componenti fragili; accesso OK
- **ombrellonidaesterno.it (Danieli)**: buon accesso, info qualitative su materiali (iroko 92x92mm), riparazione a domicilio
- Pattern di ricerca per ombrelloni pro: "[brand] ombrellone HORECA terrazze qualita" + "[brand] parasol review wind resistance professional" — entrambi restituiscono info istituzionali, non recensioni utenti
- Per Doppler usare amazon.de + testbericht.de snippets via WebSearch (no WebFetch diretto)

### TV 55 pollici fascia premium fino a 5000€, focus cinema + audio integrato (aggiornato giugno 2026)

#### Disponibilita modelli — attenzione critica
- **Sony BRAVIA 9** — NON esiste in 55". Disponibile solo in 65", 75", 85". Eliminare dalla lista se il requisito e 55".
- **Philips OLED+959** — NON esiste in 55". Solo 65". Il modello 55" con B&W e il **55OLED909** (OLED+909).
- **Panasonic MZ2000 55"** — ancora disponibile a ~1.760-2.200€ (modello 2023, in sconto). Il successore diretto e il **Z95A** (2024, ~3.300€ 55") con Fire TV OS invece di Google TV.
- **Sony A95L 55"** — disponibile ~2.600€ street price (listino 3.299€). Ultimo QD-OLED Sony della serie A (non sostituito da BRAVIA 9 in 55").

#### Prezzi street price indicativi (giugno 2026)
- Samsung S95D 55": ~1.700-1.800€
- Samsung S95F 55": ~1.300-1.700€
- LG G4 55": ~1.300-1.500€ (2024, ancora disponibile)
- LG G5 55": ~989-1.200€ (2025, forte sconto recente)
- Sony A95L 55": ~2.600€
- Philips OLED+909 55": ~1.800-2.000€ (listino 2.199€)
- Panasonic MZ2000 55": ~1.760-2.200€
- Panasonic Z95A 55": ~3.300€
- Loewe bild i 55": ~2.999€

#### Classifica audio integrato (migliore per chi NON vuole soundbar)
1. **Panasonic MZ2000 / Z95A** — 360 Soundscape Pro by Technics, 150W, 5.1.2ch con side/up-firing, beamforming. Il migliore assoluto in questa fascia. Everyeye.it: 9.5/10. "Elimina la necessita di una soundbar." Vero Dolby Atmos psicoacustico.
2. **Philips OLED+909** — B&W 3.1, 81W, titanium dome tweeter, Nautilus tube, 4 passive radiator. T3: 5/5, "Sound so impressive you'll never need a separate soundbar." AVForums: "large stereo soundstage with excellent vocal intelligibility."
3. **Sony A95L** — Acoustic Surface Audio+, 2 attuatori sul pannello + 2 woofer, 2.2ch. Suono proveniente dallo schermo stesso. "Best onboard audio ever heard from a TV." Buono per forgoing soundbar.
4. **Samsung S95D / S95F** — 4.2.2ch, 70W (S95D). S95D: "spectacular" HomeTheaterInsights ma WhatHiFi: "Audio lacks power and impact". S95F: "punchy and accurate, Atmos effects a little lacking." Solido ma non eccezionale.
5. **LG G5** — 4.2ch, 60W. WhatHiFi: audio "merely adequate", dialogue "lifeless", bass scarso. "You'll still want to consider a soundbar."
6. **LG G4** — 4.2ch, 60W. AVForums utenti: "speakers are poor." Necessita soundbar.
7. **Loewe bild i 55"** — 2x20W. Trusted Reviews: "clean, potent sound" ma 20W in totale. La Klang Bar i opzionale (+299£) necessaria per prestazioni serie.

#### Qualita immagine / colori / HDR
- **Sony A95L**: QD-OLED, DCI-P3 eccellente, HDR10/Dolby Vision, Filmmaker Mode, Cognitive Processor XR. Tom's Guide: "best picture of the year 2023". Neri perfetti OLED.
- **Samsung S95D/S95F**: QD-OLED gen3/gen4, anti-glare rivoluzionario (S95D), luminosita molto alta. WhatHiFi S95D: 5/5 "phenomenal brightness, contrast, colour." NO Dolby Vision (solo HDR10+).
- **LG G5**: OLED Primary RGB Tandem (nuova tecnologia 2025), luminosita record per OLED. AVForums: "highly recommended." Dolby Vision IQ, HDR10+.
- **LG G4**: OLED evo MLA, eccellente. Dolby Vision IQ, HDR10+. 144Hz.
- **Panasonic MZ2000**: OLED MLA custom, ~1.400 nit, DCI-P3 ~100%, DeltaE <2 out-of-box. Migliore calibrazione factory tra tutti. Dolby Vision IQ + HDR10+ Adaptive.
- **Philips OLED+909**: OLED MLA, WhatHiFi 4/5 "bright and detailed but similar to step-down model." Dolby Vision, HDR10+, Ambilight 4 lati.
- **Loewe bild i 55"**: OLED standard (no MLA), 736 nit, buoni colori ma meno luminoso dei competitor.

#### HDR e Dolby Vision — quadro completo
- Dolby Vision: Sony A95L SI | LG G4/G5 SI | Panasonic MZ2000/Z95A SI | Philips OLED+909 SI | Loewe bild i SI
- Dolby Vision: Samsung S95D/S95F NO (solo HDR10+) — critico per chi usa Apple TV

#### Fonti piu utili per questa categoria
- **T3.com** — recensioni dettagliate con voto audio esplicito, accessibile via WebFetch (Philips 909: 5/5; Panasonic MZ2000: 5/5)
- **Everyeye.it** — test italiani con misurazioni (Panasonic MZ2000: 9.5/10)
- **WhatHiFi.com** — audio-centrica, snippet utili (Samsung S95D: 5/5 immagine ma audio "lacks power")
- **Pocket-lint.com** — recensioni accessibili con voto finale e specifiche audio
- **AVForums** — 403 su WebFetch diretto per le review; usare snippet da WebSearch
- **Hdblog.it** — 429 rate limit a volte; ritentare. Buone recensioni italiane



### Fitness tracker / Smart band con sensori avanzati (aggiornato giugno 2026)

#### Scoperta critica: compatibilita iOS
- **Samsung Galaxy Fit 3**: NON compatibile con iPhone. Richiede Android. Fonte: Apple Community, Samsung US Community. Eliminare immediatamente per utenti iOS.
- **Huawei Band 9**: compatibile iOS via app Huawei Health (iOS 13+), ma NON si sincronizza con Apple Health nativo. Dati rimangono segregati in Huawei Health. Limitazione significativa per utenti che usano HealthKit come hub centrale.
- **Fitbit Charge 6**: compatibile iOS e Apple Health. Google Wallet e Maps funzionano su entrambi gli ecosistemi.
- **Garmin Vivosmart 5**: Apple Health supportato via Garmin Connect. Sincronizzazione one-way (da Garmin verso Apple Health). Da Garmin Connect v4.71 condivide anche le fasi del sonno (non solo durata).
- **Xiaomi Smart Band 9 Pro**: app Mi Fitness compatibile iOS. Sync Apple Health NON confermato da recensioni. Non citato nei test.

#### Accuratezza HR durante HIIT/CrossFit
- **Limite generale**: sensori ottici al polso degradano in modo significativo durante HIIT/CrossFit rispetto a fascia toracica. Errori tipici: 10-30 BPM durante variazioni rapide. Tendenza a lag di 10-30 secondi rispetto al valore reale.
- **Movimenti bruschi** (bar muscle-up, double under, KB swing): la band si muove e perde contatto cutaneo. Raccomandazione: portare 2 dita sopra il polso per superfice piu piatta.
- **Fitbit Charge 6**: algoritmo ML (stesso di Pixel Watch), miglioramento 60% vs Charge 5. Errore <2 BPM a riposo, ma degrada durante sprint/HIIT. Problemi segnalati di "light leakage" dovuti alla forma oblunga.
- **Garmin Vivosmart 5**: DC Rainmaker: "praticamente perfetto" su intervalli HIIT indoor. Leggero lag post-sforzo su sprint. Performance HR superiore al Fitbit Charge 5 durante esercizio (da test comparativo 2022).
- **Xiaomi Smart Band 9 Pro**: -15% errore dichiarato dal produttore. Limitazioni reali su HIIT confermata da TechRadar.
- **Amazfit Band 9**: dati insufficienti. Dalla serie Band 7 (precedente): lag HR fino a 30 secondi su HIIT, accuratezza 93% vs Polar su steady-state.

#### HRV — disponibilita per modello
- **Fitbit Charge 6**: HRV tramite app, usato per Stress Management Score. Accesso gratuito (no premium). Non broadcasting HRV verso terzi.
- **Garmin Vivosmart 5**: DC Rainmaker 2022: HRV NON supportato al lancio. Non enumera dati HRV verso terze parti (ES Elite HRV non funziona).
- **Xiaomi Smart Band 9 Pro**: HRV non citato esplicitamente nelle recensioni principali. Probabilmente solo basic.
- **Huawei Band 9**: HRV non citato nelle recensioni italiane. TruSleep 4.0 usa HR+SpO2+RR ma non espone HRV come metrica separata.
- **Samsung Galaxy Fit 3**: non rilevante (iOS incompatibile).

#### Monitoraggio sonno
- **Fitbit Charge 6**: tra i migliori per sleep tracking consumer (DC Rainmaker: "solo Oura Ring puo competere"). Ritardo elaborazione cloud per Sleep Score. SpO2 solo notturno.
- **Garmin Vivosmart 5**: riporta durata corretta, Body Battery post-sonno inizialmente bugged (fix firmware). Sleep stages da Connect v4.71.
- **Huawei Band 9**: TruSleep 4.0, monitoraggio HR+SpO2+RR notturno. Leggero per uso notturno (14g senza cinturino).
- **Xiaomi Smart Band 9 Pro**: fasi (light, deep, REM), rilevazione sonnellini diurni. 24.5g, pratico per uso notturno.

#### Prezzi indicativi giugno 2026 — Italia
- Fitbit Charge 6: ~111-173€ (idealo ~111€, Amazon ~127€, listino 160€)
- Garmin Vivosmart 5: ~120-150€ (listino 149€, in calo; modello 2022)
- Xiaomi Smart Band 9 Pro: ~50-80€ (idealo ~50€)
- Samsung Galaxy Fit 3: ~40-55€ (ma iOS incompatibile — irrilevante)
- Huawei Band 9: ~35-45€
- Amazfit Band 9: ~35-55€ (poca disponibilita in EU, piu venduta come Band 7)

#### Amazfit Band 9 — disponibilita e copertura media
- Quasi assente sulle fonti EU/IT. DC Rainmaker NON ha una recensione dedicata. Wareable, TechRadar, Tom's HW: nessuna recensione trovata.
- Possibile causa: il Band 9 e piu presente nel mercato asiatico; il successore Band 7 e il piu recensito in EU.
- Consiglio per ricerche future: cercare "Amazfit Band 9" + "zepp app" + "review" su fonti asiatiche (GSMArena, Gadgetsandwearables.com).

#### Fonti piu utili per questa categoria
- **DC Rainmaker** (dcrainmaker.com): il riferimento assoluto per test accuratezza HR. Accessibile via WebFetch. Recensione Vivosmart 5 2022 molto dettagliata con confronti HR vs Polar.
- **Altroconsumo**: ha schede per Fitbit Charge 6 (76/100), Samsung Galaxy Fit 3, Xiaomi Band 9 Pro, Huawei Band 9. Tutte accessibili via WebFetch con pattern diretto. Voti chiari.
- **TechRadar, Wareable, Gadgetsandwearables.com**: buon accesso via WebFetch per Xiaomi Band 9 Pro.
- **Notebookcheck**: accessibile, test HR comparativi vs Polar H10 (deviazione 1% per Fitbit Charge 6 a riposo).
- **Samsung Community / Apple Community**: fonti per confermare compatibilita iOS (Galaxy Fit 3 non funziona su iPhone).
- **Garmin Forums**: dati su HealthKit sync ufficiale e sue limitazioni.

#### Pattern di ricerca efficaci per questa categoria
- `"[modello] review CrossFit HIIT heart rate accuracy"` — restituisce test specifici per sport intenso
- `"[modello] Apple Health iOS HealthKit compatibility"` — essenziale per utenti iPhone
- `"[modello] altroconsumo"` + URL diretto — voto strutturato con pro/contro
- `"[modello] DC Rainmaker review"` — il test piu affidabile per atleti
- Per Samsung Galaxy Fit 3: cercare subito "[model] iOS compatible" prima di analizzare il resto — e Android-only

#### Fitness tracker cinesi di nicchia / startup — scoperte giugno 2026

- **JCVital Pro V8 ECG**: ZERO recensioni indipendenti trovate. Tutte le fonti sono il sito del produttore (jcvital.com) o il factory (jointcorp.com, Alibaba OEM). Nessun risultato su Reddit, YouTube, TechRadar, Wareable. **Red flag critico: brand senza track record consumer**. Certificazioni dichiarate: CE, FCC, RoHS, ISO13485. Non FDA-cleared come dispositivo medico. La stessa factory (Shenzhen Youhong/J-Style) produce OEM per altri brand.
- **Hume Band 2.0**: Trustpilot humeband.com = 1.4/5 "Bad". Reddit: 33% positivo su 21 recensioni. Problemi strutturali: Bluetooth disconnects costanti, app che non trova il band, nessun warning batteria scarica, supporto clienti lento/assente (no telefono). Wareable e healnourishgrow.com hanno recensioni, ma Wareable restituisce 403 su WebFetch — usare snippet WebSearch.
- **Huawei Band 11 Pro**: recensione tecnica YouTube (ID: MZeKr4FftRM) mostra HR accuracy molto bassa durante running (cadence lock, letture fino a 180bpm impossibili) e cycling outdoor (R=0.67). Accettabile solo per weightlifting (R=0.93). TechAdvisor: 4/5, TrustedReviews: 4/5 ma senza test HR. Setup iOS complicato (pairing difficile), no Apple Health nativo.
- **Honor Band 9**: HR resting ok, real-time exercise +5-10bpm sopra reale. Apple Health sync: Honor Health app NON e nella lista Apple compatible — step count non si sincronizza con Health/Fitness iOS. Problema segnalato anche su Honor Band 10. TechAdvisor: 3.5/5. Motivo principale per cui NON e raccomandato per utenti iOS.
- **Xiaomi Smart Band 10 Pro** (lancio globale maggio-giugno 2026): primo Xiaomi Band con Apple Health sync nativo confermato. HR sensor 4-LED 2-PD, claim 98.2%. Accuratezza reale: steady-state solida (3.4bpm MAE vs Polar H10), HIIT/sprint degrada (8.9bpm post-sprint). TechAdvisor: 4/5, TrustedReviews: 4/5. Globalmente disponibile da giugno-agosto 2026.
- **Huawei Band 9**: dati iOS gia nei learnings precedenti (no Apple Health sync nativo).

#### Fonti aggiuntive per tracker cinesi di nicchia
- **youtubesummary.com/summary/[videoID]**: utile per riassunti di video YouTube tecnici con test HR. Accessibile via WebFetch. Trovato tramite WebSearch con ID video YouTube.
- **redditrecs.com/fitness-tracker/model/[slug]**: aggrega recensioni Reddit per modello. Accessibile via WebFetch, contenuto spesso parziale ma sufficiente per sentiment/problemi.
- **trustpilot.com snippet** (non WebFetch diretto — spesso 403): usare WebSearch `trustpilot "[brand]" review` per snippet con rating.
- **jointcorp.com / alibaba.com**: segnale di allarme — se il prodotto e listato come OEM/ODM su questi siti, non ha track record consumer indipendente.
- **gizmochina.com**: fonte affidabile per news lancio prodotti Xiaomi con dettagli iOS support. Accessibile via WebSearch snippet.

### TV 55 pollici fascia 300-600 euro (aggiornato giugno 2026)

- **Modelli principali da analizzare**: Hisense 55U7NQ (Mini-LED ~499€), TCL 55C655 (QLED ~404€), Xiaomi TV A Pro 55 2025 (QLED ~379€), Samsung UE55DU7172 (LED ~449€), LG 55UT73006LA (LED ~399€), Hisense 55E7NQ/55E77NQ (QLED ~349-379€)
- **Altroconsumo voti**: Hisense U7NQ 74/100 | Hisense E7NQ 64/100 | LG UT73 62/100 | Samsung DU7170 58/100
- **Fascia dominata da**: Hisense, TCL e Xiaomi sotto i 400€; LG e Samsung nella fascia 400-550€
- **Tecnologie chiave**: Mini-LED = migliore contrasto ma più costoso; QLED = buon compromesso colori/prezzo; LED standard = entry-level
- **Criticità ricorrenti per categoria**: angoli di visione stretti (Samsung entry), audio debole (quasi tutti), neri non profondi su LED/QLED senza local dimming
- **Attenzione**: la Hisense U7NQ a ~499-549€ è al limite superiore della fascia ma spesso in promozione; verificare prezzo attuale prima di consigliare

### TV 55 pollici fascia 600-1000 euro, focus colori + audio (aggiornato giugno 2026)

- **Modelli da analizzare**: Samsung QE55Q80D (~680-750€), TCL 55C805 (~650-799€), LG 55QNED86A6A/T6A (~600-740€), Hisense 55U8Q (~746-850€), Samsung QE55QN90F (~990€), Samsung QE55QN85F (~985-1000€)
- **Nota disponibilità**: Sony Bravia 5 55" parte da ~1.150€ — fuori budget. TCL C855 non esiste in 55". Samsung QN90D 55" disponibile ~799€ come alternativa al QN90F.
- **Colori**: in questa fascia tutti i modelli hanno QLED/Mini-LED con Quantum Dot; la differenza reale è nel local dimming (zone): TCL C805 384 zone, Hisense U8Q 2048 zone, Samsung QN90F più zone rispetto Q80D
- **Audio senza soundbar**: Hisense U8Q è il migliore della fascia (80W, 4.1.2 reale, Dolby Atmos convincente); Samsung Q80D meglio del previsto; LG QNED86 audio sufficiente ma non eccezionale; TCL C805 audio Onkyo solo 2.0 a 15W — debole
- **Dolby Vision**: presente su TCL C805, LG QNED86A6A, Hisense U8Q, Sony X85L/X90L. ASSENTE su Samsung (tutti i modelli Samsung non supportano Dolby Vision — solo HDR10+)
- **Dolby Atmos reale**: Hisense U8Q (4.1.2, 80W), Samsung QN90F (OTS), Samsung Q80D (Dolby Atmos dichiarato, buono). LG QNED86 55" NON ha Dolby Atmos (solo i modelli QNED92/93 e QNED86 da 100")
- **Best buy colori+audio combinato**: Hisense 55U8Q è il vincitore netto per chi vuole il meglio su entrambi i fronti. Samsung Q80D è il best value se si accetta HDR10+ senza Dolby Vision
- **Attenzione**: Samsung QN90F 55" è al limite del budget (~990€); verificare promozioni. Il QN85F a ~985-1000€ è leggermente inferiore per audio ma simile per immagine

### TV QLED 55 pollici fascia 400-1000 euro, focus colori+audio esplicito (aggiornato giugno 2026)

- **Modelli analizzati in questa sessione**: Samsung Q70D (~549€), Samsung Q80D (~636-754€), Samsung QN85D Neo QLED (~730-900€), Hisense 55E7K Pro (~400-500€), Hisense 55U7Q/U7NQ (~499-600€), Hisense 55U8KQ/U8Q (~746-900€), TCL 55C745 (~400-550€), TCL 55C755 QD-Mini LED (~550-700€)
- **Altroconsumo voti**: Samsung Q80D 72/100 | Samsung Q70D 69/100 | Hisense U7NQ 74/100 | Hisense U7Q 65/100
- **Classifica colori** (migliore→peggiore nella fascia): Hisense U8Q (DCI-P3 95%, 3000 zone) > Samsung QN85D (Neo QLED mini-LED) > TCL C755 (QD-miniLED 300+ zone) > Hisense U7Q (Mini-LED, QD 90-92% DCI-P3) > Samsung Q80D (FALD, QD) > TCL C745 (QLED FALD, 94% DCI-P3) > Samsung Q70D (QLED no FALD) > Hisense E7K Pro (QLED no mini-LED, buona ma non eccellente)
- **Classifica audio integrato** (migliore→peggiore): Hisense U8Q (4.1.2 con upfiring Dolby Atmos, ~7.5/10) > Samsung Q80D (40W FALD, 5/5 Altroconsumo, "expansive and detailed" WhatHiFi 5/5) > Hisense U7Q (2.1 40W subwoofer integrato, buono) > Hisense E7K Pro (2.1 subwoofer, dialoghi chiari, 8/10 Tom's HW) > Samsung QN85D (Dolby Atmos OTS) > TCL C745 (downfiring 2x15W — PUNTO DEBOLE ESPLICITO nelle recensioni) > Samsung Q70D (audio base sufficiente)
- **Insight chiave per colori+audio combinati**: Hisense U8Q/U8KQ è il top della fascia per entrambi; Samsung Q80D è il best Samsung per audio in fascia; TCL C745 ha ottimi colori ma audio pessimo — incompatibile con richiesta utente; Hisense E7K Pro ha subwoofer integrato a prezzo accessibile ma contrasto limitato (QLED senza mini-LED)
- **Nota Samsung no Dolby Vision**: Samsung non supporta Dolby Vision in nessun modello della gamma QLED/Neo QLED — solo HDR10+. Rilevante se l'utente usa Apple TV o contenuti Apple
- **Nota fonte tecnica AV Magazine**: avmagazine.it ha un "supertest" approfondito con misurazioni per U8KQ (7.5/10) — URL accessibile via WebFetch
- **Nota fonte HW Upgrade**: hwupgrade.it ha test con misurazioni DeltaE per U8KQ — accessibile via WebFetch
