# SpecComparer — Learnings

## Fonti affidabili

### TV
- **it.hisense.com** — pagine prodotto ufficiali: restituiscono classe energetica (SDR/HDR), watt max, standby, refresh rate, HDMI 2.1, gaming features. Fetch diretto funziona bene.
- **technobattles.com** — schede tecniche dettagliate con consumo kWh/1000h, classe EU, input lag, specifiche gaming complete. Molto affidabile per TV. Per LG QNED87A6B ha funzionato bene.
- **ldlc.com** — schede tecniche europee con consumo kWh/1000h e standby. Alternativa valida quando il sito del produttore non fornisce dati energetici. Confermato per Philips 55OLED809 (kWh/1000h, standby, classe G).
- **lg.com/it** — pagine prodotto ufficiali LG: refresh rate, HDMI, gaming, standby. Consumo kWh/anno non sempre presente, ma SDR/HDR in kWh per 1000h disponibili.
- **idealo.it** — prezzi aggiornati affidabili per mercato italiano.
- **pccomponentes.it** — schede tecniche dettagliate con consumo energetico SDR/HDR. NB: restituisce 403 su WebFetch diretto.
- **supermedia.it** — spec tecniche con consumi in W, utile per verifiche rapide.
- **mediaworld.it** — ha prezzi aggiornati e classe energetica, ma il fetch tende a restituire solo CSS/navigation senza spec. Utile per prezzi da WebSearch.
- **avforums.com / techradar.com** — recensioni con misure reali (nit picco, zone dimming, DCI-P3 area). Molto utili per dati che i produttori non dichiarano. Recuperabili via WebSearch snippet.

## Fonti problematiche

### TV
- **displayspecifications.com** — restituisce HTTP 403 su WebFetch diretto. Usare WebSearch per estrarre dati dal snippet. I dati energetici (consumo W, kWh) sono presenti negli snippet se si cerca "[modello] power consumption".
- **rtings.com** — il fetch diretto restituisce solo codice JS/analytics, non le spec. Usare WebSearch per estrarre raccomandazioni dal snippet. Ottimo per misure reali (nit picco 10% window, zone dimming, DCI-P3 area).
- **kitele.com** — HTTP 403 su WebFetch. Usare WebSearch per snippet.
- **flatpanelshd.com** — pagina carica solo JS, spec non accessibili via WebFetch.
- **trovaprezzi.it** — HTTP 403 su WebFetch. Usare solo per link e snippet da WebSearch.
- **philips.it / philips.co.uk** — pagine prodotto restituiscono solo contenuto marketing via WebFetch, senza spec tecniche dettagliate (watt audio, pannello, refresh rate). Usare WebSearch + snippet per le spec mancanti.
- **tcl.com/it** — pagina prodotto restituisce solo claim marketing via WebFetch, senza numeri precisi (zone dimming, DCI-P3 %, watt). Usare WebSearch per snippet e pccomponentes/e-catalog per dati tecnici.
- **mediaworld.it** — fetch restituisce CSS e navigation, non le spec. Utile solo per recuperare prezzi via snippet da WebSearch.

## Pattern di ricerca efficaci

### TV 55" fascia budget (300-600€)
- `"[modello] scheda tecnica classe energetica consumo watt 2024 2025"` — funziona bene per trovare kWh, classe EU, standby
- `"[modello] HDMI 2.1 quante porte refresh rate nativo classe energetica kWh"` — ottimo per specifiche gaming+energia in un colpo
- `"[modello] prezzo attuale [anno] italia idealo"` — per prezzi aggiornati mercato IT
- Ricerca diretta su technobattles.com: `site:technobattles.com [marca] [modello]`

### TV 55" fascia premium (700-1000€) — QLED/Mini-LED/OLED
- `"[modello] DCI-P3 local dimming zone luminosità nit pannello VA audio watt"` — recupera spec immagine+audio in un colpo dai snippet review
- `"[modello] consumo energetico kWh anno classe energetica EU HDR SDR eprel"` — per dati energetici EU precisi
- `"[modello] prezzo idealo italia [mese] [anno]"` — prezzi real-time IT
- Per misure reali (nit, zone, DCI-P3 area): cercare su avforums.com + rtings.com via snippet, non fetch diretto
- `"[modello] DCI-P3 percentuale gamut colore specifica tecnica"` — recupera la % da recensioni italiane (hdblog.it, avmagazine.it)

## Note per categoria

### TV 55" (300-600€) — aggiornamento giugno 2026

**Modelli verificati nella fascia:**
- Samsung UE55DU7172 (2024): ~333€ — LED, 50Hz nativo, classe G
- LG 55UR78006LK (2023): ~349€ — LED, 50Hz nativo, solo HDR10/HLG, classe G
- Philips 55PUS8109 (2024): ~359-399€ — LED, 60Hz nativo, Ambilight, Titan OS, classe F
- Hisense 55E7NQ Pro (2024): ~370-480€ — QLED Full Array, 144Hz, 4x HDMI 2.1, classe F/G
- TCL 55C655 (2024): ~408€ — QLED, 120Hz, Google TV, classe F/G

**Nota: Hisense U7NQ (Mini-LED) supera i 600€ nel 2025-2026 (~807€ su idealo). Non rientra nella fascia.**

**Classi energetiche TV:** quasi tutti i TV moderni 55" ricadono in classe F o G con il sistema EU 2021. Classe E è già un buon risultato. Non aspettarsi A/B/C per pannelli LCD/QLED di questa taglia.

**Refresh rate nativo vs interpolato:** Samsung e LG dichiarano 50Hz nativi con Motion Rate/TruMotion. Verificare sempre il refresh rate nativo, non quello interpolato dal marketing.

**HDMI 2.1:** nei modelli budget (300-400€) spesso solo 1 porta HDMI 2.1 con eARC. I modelli Hisense E7NQ Pro e TCL C655 offrono 4 porte HDMI 2.1 a prezzi competitivi.

**Ambilight Philips:** vantaggio esclusivo unico nel segmento. Aggiunge valore soggettivo reale, non è solo marketing.

---

### TV 55" QLED/Mini-LED/OLED (700-1000€) — colori e audio — aggiornamento giugno 2026

**Modelli verificati nella fascia:**
- **Hisense 55U7NQ** (2024): ~808€ — Mini-LED, 200+ zone, 1.300 nit, 144Hz, audio 40W 2.1 con sub, DCI-P3 ~94%, classe E/G, VIDAA U7.6
- **Hisense 55U8Q** (2025): ~746€ — Mini-LED, ~1.092 zone, ~2.000 nit, 165Hz, audio 80W 4.1.2 con up-firing, DCI-P3 ~95%, classe E/G — **miglior spec/prezzo per colori+audio**
- **Samsung QE55Q80D** (2024): ~699€ — QLED Direct Full Array, 100 zone, ~600 nit, 100Hz, audio 40W 2.2, DCI-P3 100% vol. (VDE), classe F
- **Samsung QE55QN85D** (2024): ~730€ — Neo QLED Mini-LED, 160 zone, ~1.243 nit, 100Hz, audio 40W 2.2, DCI-P3 ~93% area, classe G HDR
- **LG 55QNED87A6B** (2025): ~543-737€ — QNED MiniLED, ~162 zone, ~800 nit, 120Hz, audio 20W 2.0, DCI-P3 ~95% vol. (Intertek), classe E — **miglior efficienza energetica del gruppo**
- **TCL 55C805** (2023): ~799€ — QD Mini-LED, 256 zone, 1.300 nit, 144Hz, audio 30W 2.0 Onkyo, DCI-P3 100% (dichiarato), classe G

**Philips 55OLED809** (2024): ~1.089€ su ldlc — fuori budget (>1.000€). OLED, 120Hz, audio 70W 2.1 4×10W+30W, DCI-P3 97%, classe G.

**Osservazioni chiave fascia premium:**
- "100% Volume Colore DCI-P3" (Samsung, TCL) ≠ "95% area DCI-P3" (LG, Hisense). Non confrontabili direttamente. Il volume colore è metrica HDR, l'area è metrica generale.
- Hisense U8Q è l'unico con up-firing speakers fisici per Atmos spaziale reale. Su tutti gli altri "Dolby Atmos" è solo decoding/pass-through.
- Samsung QN85D supera Q80D: più zone (160 vs 100), più nit (~1.243 vs ~600), stesso prezzo. Scegliere sempre QN85D su Q80D se il budget lo permette.
- LG QNED87: audio debole (20W 2.0, no Dolby Atmos), da abbinare obbligatoriamente a soundbar per uso film/serie.
- Hisense U7NQ a ~808€ è più caro dell'U8Q (~746€) pur avendo meno zone (200+ vs ~1.092) e meno potenza audio (40W vs 80W). Difficile da raccomandare rispetto all'U8Q.

---

### TV 55" QLED budget-fascia media (350-1000€) — confronto Samsung/TCL/Hisense — aggiornamento giugno 2026

**Modelli verificati (ricerca QLED 55" con budget 1000€):**

| Modello | Prezzo IT | Tecnologia | Refresh nativo | Classe EU | Note chiave |
|---------|-----------|------------|----------------|-----------|-------------|
| Samsung QE55Q60D | ~440-700€ | QLED Edge LED | 50Hz | E (87 kWh/anno) | No VRR, no 4K@120Hz, 3x HDMI, entry level |
| Samsung QE55Q70D | ~549-677€ | QLED Edge LED | 100Hz | E (89 kWh/anno) | 4x HDMI 2.1, VRR, FreeSync Premium, no Dolby Vision |
| Samsung QE55Q80D | ~753€ | QLED Direct Full Array | 120Hz | F (107 kWh/anno) | 40W 2.2ch Dolby Atmos, FreeSync Premium Pro, no Dolby Vision |
| TCL 55C645 | ~350-400€ | QLED Direct LED | 120Hz | G | 20W audio, HDMI 2.1, budget entry |
| TCL 55C745 | ~720€ | QLED Full Array | 144Hz | F/G (77W uso) | 30W, 2x HDMI 2.1, HDR10+ solo (no Dolby Vision) |
| TCL 55C755 | ~600-700€ | QD-Mini LED | 144Hz | N/D | 1300 nit, 384 zone, Onkyo 50W 2.1, Google TV, no Dolby Vision |
| Hisense 55E7KQ Pro | ~400-450€ | QLED Full Array | 100Hz | G (82 kWh/1000h SDR) | 3x HDMI 2.1, 144Hz gaming, Dolby Vision, 16W audio NO Atmos |
| Hisense 55U7NQ | ~808€ | Mini-LED ULED | 144Hz | E (63 kWh/1000h SDR) | Fuori budget 1000€, ma il migliore per efficienza energetica |
| Hisense 55U8KQ | ~886€ | Mini-LED ULED | 120Hz | G (82/150 kWh SDR/HDR) | 1500 nit, Dolby Vision IQ, 40W Dolby Atmos — sopra budget |

**Fonti usate e qualità dati:**
- samsung.com/it: dati energetici precisi, refresh rate dichiarato, audio watt. Affidabile.
- manualeitaliano.it: TCL C745 con classe F/G e 77W consumo. Affidabile.
- tvsfaq.com: Hisense U8KQ con classe G, kWh, HDMI. Affidabile.
- ldlc.com: Hisense U7NQ con classe E, 63 kWh/1000h, 40W, 4x HDMI 2.1. Ottimo.
- hwupgrade.it: Hisense U8KQ con 1500 nit, 600+ zone dimming, 2x HDMI 2.1 (144Hz). Affidabile.
- WebSearch snippet: Samsung Q80D ~1000 nit, pannello VA, 120Hz nativo.

**Attenzione marketing per questa fascia:**
- Samsung "Motion Xcelerator 144Hz" sul Q60D = interpolazione, nativo è 50Hz.
- TCL "144Hz VRR" sul C755 = gaming mode, nativo dichiarato 144Hz ma verificare.
- Hisense E7KQ Pro: HDMI sono 3, non 4 come la serie NQ. Dato fuorviante nelle schede retail.
- "100% Volume Colore Quantum Dot" (Samsung) = metrica HDR colore volume, non è 100% DCI-P3 area.
- TCL C755 ha audio Onkyo 50W con subwoofer fisico integrato — differenza reale rispetto ai 30W del C745.

**Dolby Vision nei Samsung:** assente per scelta strategica su tutta la gamma Samsung. HDR10+ è il formato preferito Samsung. Chi vuole Dolby Vision deve scegliere Hisense o TCL C645.

**Prezzi IT al 13 giugno 2026 (da idealo):**
- Samsung Q60D 55": ~440-700€ (range ampio, molti seller)
- Samsung Q70D 55": ~549-677€
- Samsung Q80D 55": ~753€
- TCL C745 55": ~720€
- TCL C755 55": ~600-700€ (stima, mercato IT variabile)
- Hisense E7KQ Pro 55": ~400-450€
- Hisense U7NQ 55": ~808€ (fuori budget)
- Hisense U8KQ 55": ~886€ (fuori budget)

---

### TV 55" OLED/QD-OLED/Mini-LED premium (1.000-5.000€) — audio integrato e qualità immagine — aggiornamento giugno 2026

**Modelli verificati nella fascia premium:**

| Modello | Prezzo IT (giugno 2026) | Pannello | Nit picco (10%) | Audio | Classe EU |
|---------|------------------------|----------|-----------------|-------|-----------|
| Samsung QE55S95D (2024) | ~1.483€ | QD-OLED 3a gen | ~1.600 nit (Std) / ~1.900 nit (Dynamic) | 70W 4.2.2 ch Dolby Atmos | G (114 kWh/anno, 82W typ) |
| Samsung QE55S95F (2025) | ~1.150€ | QD-OLED 4a gen | ~2.000 nit (stimati +30% su S95D) | 70W 4.2.2 ch Dolby Atmos | N/D |
| LG OLED55G4 (2024) | ~1.297€ | WOLED MLA 2a gen | ~1.500-1.650 nit (Std) | 60W 4.2 ch Dolby Atmos | F |
| LG OLED55G5 (2025) | ~989€ | RGB Tandem OLED | ~2.350-2.500 nit | 60W 4.2 ch Dolby Atmos | E (EPREL 2213065) |
| Sony XR-55A95L (2023/24) | ~2.599€ | QD-OLED | ~1.373 nit (Std) | 60W 2.2 ch (Acoustic Surface+) Dolby Atmos | F/G (77 kWh/1000h SDR) |
| Philips 55OLED909 (2024) | ~1.590€ (esaurito) / N/D | WOLED MLA 2a gen | ~3.000 nit (dichiarati) | 81W 3.1 ch B&W, no upfiring | G (84 kWh/1000h SDR) |
| Panasonic TX-55MZ2000E (2023) | ~2.744€ | WOLED MLA 1a gen | ~1.698-1.877 nit (Dynamic) | 160W 5.1.2 ch Technics | G (81 kWh/1000h SDR, 140 HDR) |
| Loewe bild i.55 DR+ | ~2.999€ | WOLED (WRGB) | ~736 nit | 40W 2.0 ch (integrato), +80W Klang Bar opz. | N/D |

**Note importanti scoperte in questa ricerca:**

**Sony BRAVIA 9 non esiste in 55"** — esiste solo in 65", 75", 85". Chi cerca Sony top OLED in 55" deve guardare A95L (QD-OLED, 2023) o BRAVIA 8 (WOLED, 2024).

**Philips OLED+959 non esiste in 55"** — solo in 65". Il top Philips 55" è l'OLED909 (2024), sostituito dall'OLED910 nel 2025.

**Samsung S95F vs S95D:** l'S95F (2025) è più economico (~1.150€ vs ~1.483€) con +30% nit e 4x HDMI 2.1 165Hz su tutte le porte. Scegliere sempre S95F se disponibile.

**Audio integrato — ranking reale 55":**
1. **Panasonic MZ2000** — 160W 5.1.2 Technics (40W×2 + 15W×4 + 20W sub + 2 upfiring Atmos). Unico con subwoofer fisico dedicato + upfiring veri. Audio integrato migliore assoluto.
2. **Philips OLED909** — 81W 3.1 Bowers & Wilkins (6×8.5W + 30W sub). Front-firing, NO upfiring. B&W tuning e subwoofer fisico ma no Atmos spaziale reale.
3. **Samsung S95D/S95F** — 70W 4.2.2 ch. Include upfiring (2 canali). Dolby Atmos spaziale reale.
4. **Sony A95L** — 60W 2.2 ch Acoustic Surface Audio+. Il pannello stesso vibra (no altoparlanti visibili). Molto naturale per dialogo e musica, meno spaziale senza Atmos upfiring.
5. **LG G4/G5** — 60W 4.2 ch. Include 4 canali ma senza upfiring fisici. Virtual 11.1.2 via AI.
6. **Loewe bild i.55** — 40W 2.0 ch integrati, base molto limitata. Si espande con Klang Bar i (80W opzionale).

**LG G5 vs G4:** G5 ha RGB Tandem (non MLA), drasticamente più luminoso (~2.350 nit vs ~1.650 nit), classe E invece di F, e costa meno (~989€ vs ~1.297€). G5 vince chiaramente su G4 nel 2026.

**Dolby Vision QD-OLED Samsung:** il S95D e S95F supportano HDR10+ (non Dolby Vision). Chi vuole Dolby Vision in QD-OLED deve scegliere Sony A95L.

**Loewe bild i.55 — avvisi:** refresh rate massimo dichiarato 60Hz (no 120Hz!), HDMI 2.1 a soli 18Gbps (non full bandwidth, niente 4K@120Hz). Non adatto per gaming. OS è VIDAA (Hisense). Premium di brand, non di specifiche.

**Classe energetica OLED premium 55":** quasi tutti in classe F o G con sistema EU 2021. Solo LG G5 in classe E. Il Panasonic MZ2000 è G malgrado sia 2023 — sistema audio massiccio impatta il consumo.

**Fonti usate per questa fascia:**
- samsung.com/uk: classe G, 114 kWh/anno, 82W typ, audio 70W 4.2.2 — affidabile
- lg.com/it: classe F (G4) / classe E (G5), EPREL 2213065 — affidabile
- ldlc.com: Philips 55OLED909 classe G, 84 kWh/1000h SDR, 81W B&W — ottimo
- trustedreviews.com: Loewe bild i.55 736 nit, 40W 2.0, 4x HDMI 18Gbps, €2.999 — affidabile
- snippet/review vari: Panasonic MZ2000 160W 5.1.2 Technics, Sony A95L 60W 2.2 Acoustic Surface, LG G5 2350 nit RGB Tandem — affidabili
- idealo.it: prezzi IT aggiornati giugno 2026 — affidabile

**Fonti problematiche per questa fascia:**
- displayspecifications.com: HTTP 403 su WebFetch diretto — solo snippet da WebSearch
- EPREL PDF: binario illeggibile via WebFetch — usare WebSearch snippet per dati energetici
- panasonic.com/it/specs: HTTP 403 — dati da snippet e rtings/review
- loewe.tv/it: HTTP 403 — dati da trustedreviews WebFetch

**Pattern di ricerca efficaci per fascia premium:**
- `"[modello] energy class EU kWh SDR HDR eprel"` — ottiene dati da snippet EPREL
- `"[modello] [HDMI] audio watts configuration speakers channels"` — ottiene audio e connettività
- `site:ldlc.com [modello]` — classe EU, kWh/1000h, audio W
- `site:trustedreviews.com [modello] review` — spec complete inclusa classe energetica

---

### Ombrelloni da esterno a braccio laterale/sbalzo — aggiornamento giugno 2026

**Modelli verificati (braccio laterale, 3.5m+, uso residenziale/semi-professionale):**

| Modello | Prezzo (IT 2026) | Palo alluminio | Telo | Rotazione | Inclinazione | Peso |
|---------|-----------------|----------------|------|-----------|--------------|------|
| Scolaro Leonardo Braccio 3.5x3.5 | ~1.650-1.796€ | 92x92 mm sostegno | Acrilico Dralon 350 g/m² impermeabilizzato | 360° | 20° | 70 kg |
| Scolaro Palladio Braccio 3.5x3.5 | ~1.744€ | 92x92 mm sostegno | Acrilico Dralon 350 g/m² impermeabilizzato Teflon | 360° | 20° | 80 kg |
| Scolaro Torino Braccio Ø 3.5 | ~1.290€ | 75x75 mm sostegno | Acrilico Dralon 350 g/m² impermeabilizzato Teflon | 360° | 20° | 50 kg |
| Doppler Active 370 | ~799€ | Alluminio massiccio (mm N/D) | Poliestere LSF 50+ (g/m² N/D) | 360° | Sì (leva) | N/D |
| Doppler Protect 400 | ~1.899€ | Alluminio (mm N/D) | Intrecciato 2 colori UV80+ | 360° | N/D | N/D |
| Umbrosa Paraflex Mono 2.7m | ~1.604€ | Alluminio anodizzato 2.2m | Acrilico 260 g/m² (Solidum/Sunbrella) | Braccio flessibile | Sì (pulsante) | 5.1 kg braccio |
| Umbrosa Paraflex 3.0m (wallflex) | ~1.415€ | Alluminio anodizzato | Acrilico 260 g/m² idrorepellente | Braccio orientabile | Sì | N/D |
| Fim Flexy (standard) | 3.500-7.500€ | Alluminio sez. ellittica | Acrilico 290 g/m² / Airfim (UPF 80) | N/A (sistema modulare) | Sì | N/D |

**Note critiche per categoria:**

- **Scolaro**: i modelli di serie sono principalmente acciaio + alluminio, non alluminio puro. Sostegno verticale 92x92 mm = sezione quadrata, non circolare. Equivalente a ø ~50mm. Buona robustezza.
- **Doppler Active 370**: unico modello sotto 500€ con LSF 50+, 370cm di copertura, 360°. Il palo non è 50mm (non dichiarato), probabilmente minore. Scelta budget-friendly ma non professionale.
- **Umbrosa Paraflex**: telo Sunbrella disponibile (massima qualità), design compatto, braccio flessibile molto preciso. Ma il diametro max è 3.0m (wallflex) o 2.7m (mono) — sotto i 3.5m richiesti. Prezzo superiore al budget.
- **Fim Flexy**: sistema modulare, non un ombrellone tradizionale. Prezzi da 3.500€+. Non adatto a budget 500-700€.
- **Caravita Amalfi**: palo 92x92 mm sez. quadra, rotazione 360° opzionale con pedale, telo acrilico. Prezzi non trovati online (distribuzione indiretta, richiede preventivo).
- **UPF**: nessun produttore nella fascia semi-pro dichiara esplicitamente UPF 50+. Il Doppler lo chiama LSF 50+. Umbrosa certifica ISO 105 B02/B04. Scolaro dice solo "impermeabilizzato" senza certificazione UPF numerica.

**Budget 500-700€ per braccio laterale 3.5m:**
- Praticamente impossibile con brand semiprofessionali italiani/europei. Scolaro/Caravita iniziano da ~1.200€.
- Doppler Active 370 a ~800€ è il più accessibile tra i prodotti verificabili, ma non raggiunge i 3.5m (è 3.7m rettangolare non rotondo).
- Budget 500-700€ copre ombrelloni di fascia consumer (es. Leroy Merlin, generici cinesi) non i brand richiesti.

**Fonti affidabili per ombrelloni:**
- designperte.it — spec dettagliate prodotti Scolaro, prezzi scontati, affidabile
- caffegrazie.it — prezzi e spec Scolaro, affidabile
- bsvillage.com — spec Umbrosa Paraflex con prezzi IT, molto buono
- umbrosashop.com — schede tecniche ufficiali Umbrosa, affidabile
- dopplershop.it — JS-heavy, non leggibile via WebFetch (restituisce solo JS analytics)
- dopplerschirme.com — pagine prodotto leggibili parzialmente, spec incomplete

**Fonti problematiche per ombrelloni:**
- dopplershop.it — restituisce solo JS, non spec. Usare WebSearch snippet.
- mk2shop.com — HTTP 403 su WebFetch
- edilportale.com — pagina produttore senza spec, solo descrizione marketing

**Pattern di ricerca efficaci:**
- `"[marca] [modello] braccio laterale specifiche palo alluminio mm peso telo"` — funziona per Scolaro
- `"[brand] cantilever umbrella specifications aluminum pole fabric UPF weight"` — per brand internazionali (Doppler, Umbrosa)
- `site:designperte.it [modello]` — ottimo per specifiche Scolaro complete
- `site:bsvillage.com [marca]` — ottimo per Umbrosa con prezzi IT
