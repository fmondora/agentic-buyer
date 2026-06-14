# TechnicalCritic — Learnings

## Fonti affidabili

### TV QLED/Mini-LED
- **RTings.com** — misurazioni oggettive complete (nits, contrasto nativo, Delta E, uniformità, motion). Accesso via WebSearch snippet: cercare "[modello] RTings review measurements" per estrarre dati chiave senza WebFetch.
- **AVForums.com** — recensioni UK con misurazioni, ottimo per modelli europei (es. QE prefix Samsung). Snippet utili su prezzo, judder 24p, calibration.
- **FlatpanelsHD.com** — test europei approfonditi, buona copertura misurazioni calibrate. Modello TCL C805 testato.
- **TechRadar.com** — recensioni pratiche con nits misurate, utile per confronti rapidi e dati uniformità.
- **Tom's Guide** — buoni dati pratici, particolarmente utile per gaming e HDR.
- **HDBlog.it** — fonte italiana utile per prezzi EU e disponibilità modelli Hisense (es. 55U7NQ).
- **Trovaprezzi.it / Idealo.it** — per prezzi correnti mercato italiano.
- **What Hi-Fi** — giudizi qualitativi pratici su audio e visione reale, meno tecnico ma affidabile.
- **Expert Reviews UK** — buon mix misurazioni + giudizio pratico per TV mid-range europei.
- **Reviewed.com** — misurazioni peak brightness standardizzate (10%, 25%), affidabili per nit reali.
- **displayspecifications.com** — spec tecniche pannello (tipo, zone, refresh rate) quando i siti di recensioni non coprono il modello esatto.
- **AVForums.com** — recensioni UK dettagliate con misurazioni, ottimo per modelli premium OLED (MZ2000, G4, S95D). Snippet ricchi di dati nit e calibrazione.
- **FlatpanelsHD.com** — ricco di dati misurati per OLED premium; copre bene anche modelli europei recenti (S95F 2025, LG G5, Panasonic Z95A/Z95B).
- **T3.com** — giudizi qualitativi audio e immagine, utile per comparazioni veloci.
- **TechRadar.com** — buona copertura modelli premium, dati brightness in più modalità.
- **Pocket-lint.com** — buone recensioni audio (Panasonic MZ2000), giudizi pratici uso quotidiano.
- **trovaprezzi.it** — prezzi correnti mercato italiano, affidabile per street price OLED premium.

## Fonti problematiche

- **WebFetch su RTings.com** — non funziona (JS rendering). Usare solo WebSearch per snippet.
- **WebFetch su AVForums** — pagine forum non estratte bene. Preferire ricerche mirate per pagine review.
- **Samsung.com / Hisense.com diretti** — solo spec marketing, nessuna misurazione reale.
- **Consumer Reports** — paywall, risultati bloccati.
- **HDTVTest sito** — non trovato nei snippet in modo consistente. Cercare via YouTube.

## Pattern di ricerca efficaci

- `"[modello] RTings review measurements contrast peak brightness [anno]"` — estrae nits, contrasto, Delta E
- `"[modello] RTings score [funzione specifica] nits"` — più mirato per singola metrica
- `"[modello] AVForums review [anno] measurements"` — ottimo per modelli europei con prezzo £/€
- `"[modello] calibration Delta E Filmmaker Mode review"` — per dati post-calibrazione
- `"[modello] europe brightness limitation HDR"` — per scoprire cap regionali (problema noto TCL EU)
- `"[modello] prezzo italia euro disponibilità"` — per verifica disponibilità mercato italiano
- `"[modello] peak brightness nits HDR10 measured"` — per dati brightness reali da Reviewed/Digital Trends
- Ricercare sempre anche il modello successivo/precedente della stessa serie se il modello esatto non ha review RTings
- Per TCL Europa: C755 = C805 nel resto del mondo. Cercare entrambi.
- Cercare sia il modello europeo (es. QE55Q80D) che USA (QN55Q80D) per più risultati

## Note per categoria

### Ombrelloni da esterno palo laterale/cantilever 3.5m+ (aggiornamento giugno 2026)

**Brand valutati:** Scolaro (IT), Caravita (DE), Suns/SUNS (NL), Fim (IT), Umbrosa (BE), Doppler (AT)

**Fonti utili per questa categoria:**
- **fim-umbrellas.com** — sito ufficiale FIM con schede tecniche (parzialmente accessibile via WebFetch)
- **greenterest.it** — rivenditore italiano con schede prodotto FIM Capri e Rodi, prezzi
- **parasol-pro.it / parasol-pro.co.uk** — rivenditore EU con prezzi e confronti tra brand (Scolaro, Umbrosa, ecc.)
- **caravita.eu** — sito ufficiale Caravita, schede tecniche modelli Amalfi
- **dopplerschirme.com** — sito ufficiale Doppler con prezzi (Expert 350 = €1.599)
- **hello-suns.com** — sito ufficiale SUNS garden furniture NL, modelli Palmoli e Novara
- **ombrapro.it** — rivenditore IT basi e zavorre Scolaro (piastra cemento 60kg = €140)
- **umbrosashop.com** — shop ufficiale Umbrosa, specifiche Spectra

**Fonti problematiche per questa categoria:**
- Non esistono siti equivalenti a RTings.com per ombrelloni — nessun test indipendente standardizzato
- Forum italiani: non trovati thread specifici su problemi snodi cantilever
- EN 581 non citato da nessun produttore analizzato (standard più pertinente sarebbe EN 13561 per tende da sole)
- Pyracantha.co.uk — sito JS, WebFetch restituisce solo JS/metadata, nessun contenuto review

**Identità brand — chiarimenti critici:**
- **Suns** = SUNS garden furniture (Olanda, hello-suns.com). Modelli: Palmoli (3x3/3x4, palo centrale), Novara (4x3, palo centrale con LED). NESSUN modello cantilever/a sbalzo nel range 500-700€. Modelli top >€1.500
- **Doppler** = brand austriaco, sito dopplerschirme.com. Modello Expert 350cm cantilever = €1.599. Non nel range 500-700€
- **Umbrosa** = brand belga. Spectra max 3x3m (NON 3.5m disponibile). Prezzo molto elevato (>€1.500)
- **Caravita** = brand tedesco premium. Amalfi disponibile in 350x350. Base standard 33-43kg (INSUFFICIENTE per montagna)
- **Scolaro** = brand italiano, fondata 40+ anni fa. Galileo e Capri disponibili in 350x350. Prezzi da €1.433-€2.100+
- **Fim** = brand italiano. Capri e Rodi con palo 76x76mm alluminio. Prezzi da €1.434 (Capri 350x350)

**Dati tecnici struttura — valori critici per uso montagna:**
- Palo professionale minimo: 76x76mm alluminio (FIM, Scolaro) vs 50-60mm entry-level
- Base zavorrabile professionale: minimo 60kg per 3.5m; consigliata 80-100kg+ per vento raffica
- Caravita Amalfi mast: 60x100mm, 4mm spessore parete — trave rettangolare, geometria insolita
- Umbrosa Spectra: profilo basso "sheer" per ridurre resistenza vento — design specifico anti-vento
- Doppler Expert 350: sistema cinghia dentata (tooth belt drive) per rotazione — innovativo
- Beaufort dichiarato dai brand: Umbrosa 4-7 (Bft); altri non dichiarano valori specifici
- NESSUN brand analizzato cita certificazione EN 581 (che riguarda sedute da esterno, non ombrelloni)

**Budget 500-700€ per 3.5m palo laterale — realtà del mercato:**
- NESSUNO dei 6 brand richiesti (Scolaro, Caravita, Suns, Fim, Umbrosa, Doppler) è disponibile in 3.5m a palo laterale entro 500-700€
- Tutti questi brand sono fascia premium/professionale: prezzi reali 1.400-2.500€+
- A 500-700€ entrano brand mid-range: Ombrellificio Veneto, BIA store, alcune linee Leroy Merlin
- Il range 500-700€ copre ombrelloni 3x3m entry-level di questi brand o varianti semplificate

**Problemi strutturali specifici cantilever da vento (consensus fonti):**
- Punto critico 1: snodo inclinazione — nelle versioni economiche è in plastica rinforzata, si degrada con UV+cicli apertura
- Punto critico 2: giunto rotazione base — usura meccanica dopo 2-3 stagioni se non ingrassato
- Punto critico 3: braccio orizzontale — dimensionamento della sezione rispetto al telo (momento flettente aumenta con 3.5m)
- Vento e inclinazione: inclinare il telo al vento crea "parachute effect" — il telo inclinato è la configurazione più pericolosa in caso di raffica
- Base 60kg è il minimo raccomandato per 3.5m; per vento Beaufort 5+ serve 80-100kg con ancoraggio
- La struttura a palo centrale resiste meglio al vento rispetto al braccio laterale (geometria baricentrica)

### TV OLED/QD-OLED/Mini-LED premium 55" budget 3000-5000€ (aggiornamento giugno 2026)

**Modelli valutati:**

| Modello | Anno | Pannello | Nit HDR 10% misurati | Audio integrato | Prezzo IT indicativo |
|---|---|---|---|---|---|
| Samsung S95D | 2024 | QD-OLED Gen3 (glare-free) | ~1868 nit (Standard), ~1688 nit (Filmmaker) | 4.2.2 ch 60W — audio mediocre, bassi assenti | ~1800-2200€ (55") |
| Samsung S95F | 2025 | QD-OLED Gen4 (glare-free 2.0) | ~2000-2388 nit (10% HDR) | 4.2.2 ch 70W — leggero miglioramento ma sempre debole | ~1363-2100€ (55") |
| LG OLED G4 | 2024 | WOLED MLA (Meta 2.0) | ~1488 nit (Filmmaker Mode) | 4.2 ch 60W — accettabile, mai ottimo, soundbar necessaria | ~1400-1800€ (55") |
| LG OLED G5 | 2025 | RGB Tandem OLED (4-stack) | ~2200-2350 nit (calibrated), ~2500 nit (vivid) | 4.2 ch 60W — downfiring, giudizi discordanti (da ok a "appalling") | ~1187-1400€ (55") |
| Sony A95L | 2023 | QD-OLED Samsung Display | ~1215-1373 nit (10% HDR calibrated) | Acoustic Surface Audio+ 2 attuatori + 2 woofer — TRA I MIGLIORI TV per audio nativo | ~2500-3500€ (55") |
| Sony BRAVIA 9 | 2024 | Mini-LED Full Array | ~2816 nit (10% HDR), ~1871 nit (Movie mode) | Acoustic Multi-Audio+ 70W — buono ma back-firing, controverso | ~3000-4500€ (55") |
| Philips OLED+909 | 2024 | WOLED MLA (Meta 2.0) | ~1087 nit (10%), ~2008 nit (1%) | B&W 3.1 ch 81W — MIGLIORE TV per audio nativo, nega soundbar | ~2500-2945€ (55") |
| Panasonic MZ2000 | 2023 | WOLED MLA (Master OLED Ultimate) | ~1426 nit (Filmmaker, AVF), ~1700 nit (Dynamic) | Technics 360 Soundscape Pro 150W 5.1.2 — MIGLIORE TV per audio nativo (testa a testa con B&W) | ~2500-3000€ (55") |
| Panasonic Z95A/Z95B | 2024/2025 | WOLED MLA / RGB Tandem | ~1700 nit MLA (Z95A), ~2107 nit Tandem (Z95B) | Technics 360 Soundscape Pro 5.1.2 — eccellente, pari a soundbar mid-range | ~2800-4000€ (55") |
| Loewe bild i | 2021-2024 | WOLED standard | Non misurato — performance standard WOLED ~800-1000 nit | 20W integrato — INSUFFICIENTE senza Klang Bar i | ~2999£ UK / non standard IT |

**Differenze pannello chiave (WOLED vs QD-OLED) — confermate da test:**
- QD-OLED (Samsung S95D/F): angoli di visione simili a WOLED su OLED; DCI-P3 color volume superiore su highlight; picco brightness più alto su finestre piccole; glare-free screen S95D/F rivoluzionario per stanze illuminate
- WOLED MLA (LG G4, Philips 909, Panasonic MZ2000): brightness full-screen più uniforme, vantaggio per sport/contenuti SDR; colori leggermente meno saturi nei picchi HDR; angoli di visione eccellenti
- RGB Tandem (LG G5, Panasonic Z95B): evoluzione WOLED con doppio layer — brightness record ~2200-2500 nit calibrated; supera QD-OLED su brightness ma DCI-P3 color volume ancora inferiore
- Mini-LED (Sony BRAVIA 9): brightness assoluta record (2816 nit 10%); blooming controllato grazie a XR Backlight Master Drive; contrasto nativo infinito impossibile (LCD backlit); per stanze molto luminose è il re

**Audio integrato — ranking reale (senza soundbar):**
1. Panasonic MZ2000/Z95A/Z95B — Technics 360 Soundscape Pro 150W 5.1.2: il più completo, larghezza + altezza + bassi reali, sostituisce soundbar mid-range
2. Philips OLED+909/910 — B&W 3.1 81W: suono musicale, chiarezza vocale eccellente, bassi sorprendenti per un TV; alcuni reviewer preferiscono soundbar premium ma non è obbligo
3. Sony A95L — Acoustic Surface Audio+: il pannello suona, dialoghi cristallini e incollati all'immagine, soundstage ampio e alto; difficile battere per cinema senza soundbar
4. Sony BRAVIA 9 — Acoustic Multi-Audio+ 70W: buono per dimensioni, back-firing controverso, dialoghi chiari ma bassi poco estesi
5. Samsung S95F/D — 4.2.2 ch 60-70W: accettabile, dialoghi ok, bassi insufficienti, spazialità limitata; soundbar caldamente consigliata
6. LG G5/G4 — 4.2 ch 60W: il punto debole della linea, downfiring limita staging; soundbar necessaria per chi vuole audio da cinema
7. Loewe bild i — 20W stereo: insufficiente, richiede Klang Bar i (soundbar proprietaria)

**Pattern critici per questa categoria:**
- Samsung S95D/F: leader assoluto per stanze illuminate (glare-free screen), QD-OLED brightness, gaming (165Hz VRR). Audio è il punto debole. NO SOUNDBAR = esperienza audio mediocre.
- LG G5: pannello Tandem rivoluzionario per brightness, ma audio ancora il tallone d'Achille. Ha eliminato DTS (solo Dolby).
- Sony A95L: QD-OLED con processore XR — la combinazione Cognitive XR + Acoustic Surface è unica per cinema. Modello 2023 ma ancora riferimento.
- Sony BRAVIA 9: Mini-LED con brightness record — per stanze luminose è il migliore non-OLED. Audio controverso.
- Philips OLED+909: Ambilight + B&W audio = esperienza cinematografica senza soundbar. Nit leggermente inferiori ai top (1087 nit 10%).
- Panasonic MZ2000/Z95A/Z95B: CINEMA puro — Dolby Vision IQ, calibrazione Calman, HDR Filmmaker Mode accuratissimo + audio Technics senza rivali. Scelta ideale per chi NON vuole soundbar.
- Loewe bild i: nicchia premium design, audio 20W insufficiente, prezzo altissimo per performance non top. Non consigliabile nel contesto.

**Filmmaker Mode — qualità implementazione (ranking):**
1. Panasonic (MZ2000/Z95) — il gold standard, anche Calman AutoCal
2. Sony (A95L/BRAVIA 9) — Cognitive XR + Netflix Calibrated Mode + Calman
3. Philips OLED+909 — buona implementazione, ISF certified
4. LG G4/G5 — buono, ora Dolby Vision + Filmmaker Mode combinati (novità G4)
5. Samsung S95D/F — presente ma meno raffinato; tone mapping aggressivo in certi contenuti

**Giudder 24p:**
- Samsung S95D/F: storica debolezza Samsung, necessita regolazione manuale de-judder
- LG G4/G5: gestione 24p eccellente
- Sony A95L/BRAVIA 9: eccellente via Motionflow Cinematic
- Panasonic MZ2000/Z95: eccellente, tra i migliori in assoluto
- Philips OLED+909: buona gestione

**Angoli di visione:**
- OLED (tutti i tipi): quasi identici tra WOLED e QD-OLED — entrambi eccellenti, degradano solo oltre 60-70° (non rilevante uso normale)
- Mini-LED Sony BRAVIA 9: buono per LCD ma inferiore a qualsiasi OLED; degrado visibile oltre 40°

### TV QLED/Mini-LED 55" sotto 1000€ (aggiornamento giugno 2026)

**Modelli validi nel range:**
- **Hisense 55U7NQ** (Italia): ~550-600€, 240 zone dimming, 1500 nit dichiarati, 1130 nit Filmmaker Mode misurati. Best buy assoluto per rapporto qualità/prezzo.
- **Hisense 55U8N** (disponibile USA/UK, non sempre IT 55"): ~700-800€ UK, 1600 zone, ~3700 nit picco misurato RTings (65"). Il 55" ha spec leggermente inferiori.
- **Samsung QE55QN85D** (Neo QLED): ~850-999€ IT, 330 zone (55"), 872 nit picco misurato, niente Dolby Vision (limitazione Samsung — solo HDR10+).
- **Samsung QE55QN90D** (Neo QLED premium): >1000€ full price ma in offerta intorno a 999€, 792 zone (65"), ~2100-2500 nit picco. Niente Dolby Vision.
- **Sony XR-55X90L** (Bravia Full Array): ~800-950€ (modello 2023, ancora disponibile), ~1600 nit HDR misurato, Dolby Vision eccellente, calibrazione fabbrica buona.
- **TCL 55C805K** (Mini-LED QD): ~650-800€, 384 zone, 819 nit su 10% finestra misurati (modello EU ha cap brightness vs USA). **Attenzione: TCL EU limita firmware HDR brightness**.

**Dati misurati specifici per la fascia Q60/Q70/Q80/C645/C745/C755/E7K/U7K/U8K:**

| Modello | Tecnologia | Zone | Nit HDR picco (10% finestra) | Dolby Vision | Filmmaker Mode | Note chiave |
|---|---|---|---|---|---|---|
| Samsung Q60D 55" | QLED VA edge-lit | nessuna | ~470 nit | NO | Si | entry-level, no FALD |
| Samsung Q70D 55" | QLED VA edge-lit | nessuna | ~500-600 nit (stima) | NO | Si, DeltaE 1.97 | no FALD malgrado prezzo mid-range |
| Samsung Q80D 55" | QLED VA FALD | 100 | ~1000 nit | NO | Si | blooming contenuto, audio 40W buono |
| TCL C645 55" | QLED VA global dimming | nessuna | ~400-450 nit | Si (DV IQ) | NO | entry level, no FALD |
| TCL C745 55" | QLED VA FALD | 120 | ~700-800 nit (stima) | Si (DV IQ) | NO | 144Hz, 2xHDMI 2.1, ottimo gaming |
| TCL C755/C805 55" | QD Mini-LED FALD | ~300-500 zone | ~1300 nit | Si (DV IQ) | NO (Movie Mode ok) | top TCL fascia, ColourSpace calibrazione |
| Hisense E7K 55" | QLED Direct LED | poche/nessuna | ~330-400 nit | Si (DV IQ) | non confermato | entry Hisense, contrasto 3800:1 |
| Hisense U7K 55" | Mini-LED FALD | ~280-384 zone | ~585 nit Filmmaker Mode | Si (DV IQ) | Si, preciso | miniLED base, brightness modesta |
| Hisense U8K 55" | Mini-LED FALD | 1008 zone | 1590-1788 nit misurati | Si (DV IQ) | Si, DeltaE 4.1 OOB → 2.0 calibrato | re della fascia per HDR reale |

**Pattern critici per questa categoria:**
- Samsung non supporta Dolby Vision su nessun modello (nemmeno top di gamma) — grande limitazione per chi ha Netflix/Apple TV+.
- TCL EU ha problemi storici di firmware cap sulla luminosità HDR — verificare sempre versione firmware attuale.
- TCL C755/C805 NESSUN Filmmaker Mode — confermato da FlatpanelsHD/AVForums. Movie Mode è sostituto accettabile.
- Hisense U8K: Filmmaker Mode inaccurato out-of-box (Delta E 4.1, troppo rosso) ma eccellente dopo calibrazione.
- Hisense U8N non è sempre disponibile in 55" in Italia — verificare stock.
- Sony X90L è modello 2023 ma ancora ottima scelta per cinema grazie a Dolby Vision + calibrazione eccellente.
- Hisense U8K 55" è il TV con più nit reali misurati nella fascia sotto 1000€ (1590-1788 nit).
