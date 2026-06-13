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
