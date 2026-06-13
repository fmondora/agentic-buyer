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

## Note per categoria

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
