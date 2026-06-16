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

---

### Tavole/pannelli in larice per rivestimento parete interno — aggiornamento giugno 2026

**Fonti affidabili:**
- **trumerholz.com** — schede prodotto complete con prezzi/m², dimensioni (spessore, larghezza, lunghezza), finiture (spaccato/spazzolato/evaporato). Larice alpino da Alto Adige. Prezzi visibili senza login.
- **pellet-legnami.it** — classi qualità AB e BC esplicite, prezzi per pezzo, umidità dichiarata (18%), dimensioni complete. Larice siberiano. Molto affidabile.
- **bewoodshop.it** — confronto grezzo vs piallato stesso prodotto (€4 vs €7,15 per 100cm per tavola 25×100mm). Tolleranza +/-3mm su lunghezza e sezione. Nessuna info umidità/provenienza.
- **gallolegnami.it** — densità larice secco 650 kg/m³, modulo elastico 14.000 N/mm². Dati strutturali affidabili.
- **risponde.promolegno.com** — fonte autorevole per confronto alpino vs siberiano. Durabilità EN 350-2 classe 3-4 per entrambi. Siberiano: nodi piccoli, struttura omogenea, maggior stabilità dimensionale.
- **pandawood.it** — umidità consigliata per interno 12-15%, densità 650 kg/m³.
- **nordholz.it** — rivestimenti larice alpino Alto Adige, prezzi/m² (€191-248/m²), finiture premium (spaccato+spazzolato, evaporato). Nessun dato umidità/qualità.

**Fonti problematiche:**
- **xlab.design** — HTTP 404 su pagine prodotto dirette. Usare snippet WebSearch per dimensioni (tavole 150x17x25mm).
- **bricolegnostore.it** — URL prodotti singoli restituiscono 404. Pagina categoria funziona.
- **shop.ramoserholz.com** — prezzi nascosti (richiedono login/account). Classi qualità visibili nei titoli prodotto via WebSearch.
- **putzer.com** — pagine prodotto restituiscono solo JS/CSS. Prezzi estraibili solo da snippet WebSearch.
- **mazzucatolegnami.it** — prezzi e spec incomplete. Solo lista prodotti senza dettagli tecnici.

**Pattern di ricerca efficaci:**
- `"[fornitore] larice [dimensioni] prezzo"` — snippet da WebSearch per prezzi
- `site:pellet-legnami.it larice` — prezzi e classi qualità leggibili
- `"larice siberiano vs alpino [uso specifico]"` + WebFetch su risponde.promolegno.com
- `"larice [dimensioni] rivestimento parete interno essiccato"` — trova fornitori con spec umidità

**Note categoria — tavole larice rivestimento parete:**

**Classi qualità (norma EN 13017-1 per conifere):**
- **Classe A / 0-I**: senza nodi, pochi difetti — uso premium, prezzo +30-40%
- **Classe B / I-II**: nodi sani fino a 25 mm, piccole riparazioni — uso standard
- **Classe C / II**: nodi fino a 45 mm, forte variazione colore — rustico/economico
- **AB** (nomenclatura mercato estero): corrisponde a B italiano, qualità superiore
- **BC**: corrisponde a C italiano, rustico con nodi
- **US / Boules**: selezione grezza non piallata, classi miste 0-II

**Umidità target per interno:**
- Secco in forno (KD) 8-12%: ideale per riscaldamento, ambienti secchi. Evita ritiro post-posa.
- Naturale/stagionato 15-20%: accettabile per ambienti temperati. Rischio lieve ritiro.
- Pellet-legnami.it dichiara 18% (naturale). Putzer non dichiara. Trumerholz non dichiara.
- Per parete interna riscaldata: chiedere esplicitamente KD ≤12%.

**Densità e peso:**
- Larice alpino (Larix decidua): 550-650 kg/m³ secco
- Larice siberiano (Larix sibirica): 650-725 kg/m³ secco — più denso del 7-9%
- Calcolo peso tavola 80×200×18mm: volume = 0,08×0,20×0,018 = 0,000288 m³ → 650 kg/m³ × 0,000288 = **0,187 kg per tavola** (alpino) / **0,205 kg** (siberiano)

**Differenza prezzo grezzo vs piallato:**
- Dati bewoodshop.it su tavola 25×100mm: grezzo €4,00 / piallato €7,15 per 100cm → **+79% per piallato S4S**
- Su formati maggiori il delta si riduce (lavorazione ha costo fisso). Stima realistica: +30-50% per S4S.
- Spazzolato: +15-25% aggiuntivo rispetto a piallato (lavorazione estetica).

**Provenienza — differenze pratiche:**
- **Alpino** (Austria, Italia settentrionale, Tirolo): anelli larghi, nodi frequenti e grandi, colore rosso-arancio intenso. Più economico sul mercato IT. Classi A più rare.
- **Siberiano** (taiga russa): anelli stretti, nodi piccoli, struttura omogenea, stabilità dimensionale superiore. Adatto per interni con riscaldamento. Richiedere FSC/PEFC.
- **Scandinavo** (Finlandia, Norvegia): non è larice ma spesso pino nordico. Non confondere con larice scandinavo.
- Durabilità EN 350-2: classe 3-4 per entrambi alpino e siberiano — non idonei per uso esterno senza trattamento.

**Formati disponibili sul mercato (effettivi, non 80×200×18mm esatti):**
- Spessori comuni: 18-19 mm, 22-25 mm, 28-32 mm
- Larghezze comuni: 90-100 mm, 140-150 mm, 175-200 mm
- Lunghezze: 2000-4000 mm
- Per parete 80mm di larghezza: raro come formato standard. Di solito 90-100mm. Su misura disponibile.
- La dimensione 200cm di lunghezza è disponibile ma meno comune di 400cm.

**Etichetta energetica EU:** N/A — prodotti in legno non soggetti a etichettatura energetica EU (direttiva 2010/30/UE si applica a prodotti energetici, non a materiali da costruzione passivi).

---

### Fitness tracker / Recovery band screenless per CrossFit (budget ≤200€) — aggiornamento giugno 2026

**Modelli verificati (shortlist CrossFit + salute 24/7, iOS, HRV/SpO2/VO2max):**
- Amazfit Helio Strap (~€100) — screenless, BioTracker 6.0 PPG 5 fotodiodi, 20g, HRV sonno, SpO2 periodico, VO2max (richiede corsa 10min 75% HRmax + telefono), iOS HealthKit sì, no GPS, ~10 giorni batteria, no subscription
- Google Fitbit Air (~€100) — screenless, 12g con strap (5.2g senza), GPS connected, HRV sonno, SpO2 periodico, NO VO2max, iOS 16.4+ HealthKit (read-only, non write), ~7 giorni batteria, no subscription (Premium opzionale €9.99/mese)
- WHOOP 5.0 (~€199/anno) — screenless, PPG 26Hz, 26.5g, IP68 10m, HRV continuo 24/7, SpO2 continuo, VO2max sì, iOS 14+ sì, NO GPS, 14 giorni batteria, subscription obbligatoria €199/anno (hardware incluso)
- Fitbit Charge 6 (~€85-130) — display AMOLED 1.04", 30g con strap, GPS built-in, HRV sonno, SpO2 notturno, VO2max sì (Cardio Fitness Score), iOS sì ma NO HealthKit nativo (solo app terze parti a pagamento), 5ATM, 7 giorni batteria, no subscription (Premium opzionale)
- Garmin Vivosmart 6 (leak, ~€179, non ancora disponibile) — GPS built-in (confermato da leak), 30+ sport modes, HRV Status atteso (non confermato), SpO2 atteso, VO2max atteso, iOS sì, prezzo stimato €149-199

**Note critiche per categoria CrossFit/recovery band:**

**HRV — tipologie distinte da non confondere:**
- HRV "continuo 24/7" vero: solo WHOOP 5.0. Raccoglie dati HRV ogni minuto, calcola recovery score al risveglio su dati notturni.
- HRV "sonno only": Amazfit Helio, Fitbit Charge 6, Fitbit Air — misurano HRV durante il sonno, non durante il giorno.
- Garmin Vivosmart 5: HRV usato internamente per Body Battery/stress, non esposto come HRV Status separato. Il 6 dovrebbe aggiungere HRV Status ufficiale.

**Optical sensor + CrossFit — problema noto:**
- Tutti i wristband (polso) hanno accuracy ridotta durante movimenti esplosivi CrossFit (sollevamento, box jump, kettlebell swing): oscillazioni del polso interferiscono col sensore PPG.
- WHOOP soluzione documentata: posizionare sul bicipite — elimina interferenze grip/forearm, accuracy ~99% chest strap.
- Fitbit Charge 6: sensore migliorato "60% più accurato" per HIIT, ma community reports mostrano problemi reali durante WOD con barbell. Wrist placement critico.
- Amazfit Helio Strap: PPG BioTracker 6.0, 5 fotodiodi — migliore hardware tra i budget, ma non testato sistematicamente per CrossFit specifico.
- Fitbit Air: overshot di 20-40bpm durante interval ad alta intensità confermato da DC Rainmaker.

**VO2max — metodi e affidabilità:**
- WHOOP 5.0: stima continua su 145+ attività, metodo più completo.
- Garmin Vivosmart 6: atteso come il 5 (richiede attività cardio ≥15 min).
- Fitbit Charge 6: "Cardio Fitness Score" — stima, non clinica, ma confermata funzionante.
- Amazfit Helio: richiede corsa specifica ≥10min + telefono, VO2max sistematicamente sottostimato (test DC Rainmaker: 40 vs 47 Garmin+chest strap).
- Fitbit Air: NO VO2max confermato.

**iOS/HealthKit — differenze importanti:**
- Amazfit Helio: HealthKit write sì (sleep, HRV, HR, VO2max, SpO2, resp rate, steps).
- WHOOP 5.0: HealthKit sì (iOS 14+).
- Garmin Vivosmart 6: HealthKit sì (tutti i Garmin post-2020).
- Fitbit Charge 6 / Fitbit Air: NO HealthKit nativo — solo app terze parti a pagamento (es. "Fitbit to Apple Health Sync"). Gap rilevante per utenti iOS.

**Subscription model WHOOP — costo totale EU:**
- WHOOP One: €199/anno — hardware incluso (WHOOP 5.0 device).
- Dopo primo anno: si rinnova €199/anno. Su 2 anni = €398 totale.
- Tier superiori (Peak, Life) costano di più e includono WHOOP MG (con sensori medici aggiuntivi).
- Nessun costo anticipato per device fisico — modello opposto a tutti gli altri.

**Fonti affidabili per questa categoria:**
- dcrainmaker.com — recensione approfondita Amazfit Helio Strap con test VO2max e GPS accuracy
- dcrainmaker.com/2026/05/fitbit-review-vs-whoop.html — Fitbit Air vs WHOOP: dati accuracy HIIT
- wearabledevices.com/devices/whoop-5 — spec complete WHOOP 5.0
- smartwatchinsight.com/garmin-vivosmart-6/ — leak confermati Vivosmart 6 (GPS, 30+ sports)
- community.fitbit.com — conferma assenza HealthKit nativo Fitbit
- the5krunner.com — accuracy test WHOOP 5.0 in condizioni reali

**Fonti problematiche:**
- us.amazfit.com/products/helio-strap — restituisce solo JS Shopify, nessun dato spec
- store.google.com/product/google_fitbit_air_specs — redirect consent cookie, non accessibile
- wearablexp.com — JS-heavy, solo CSS/schema, no body article

**Pattern di ricerca efficaci:**
- `"[modello] HRV continuous 24h or sleep only"` — distingue tipi HRV
- `"[modello] CrossFit weightlifting HR accuracy optical sensor"` — accuracy movimenti esplosivi
- `"[modello] iOS HealthKit native sync confirmed"` — verifica integrazione reale
- `"WHOOP subscription cost EU per year [anno]"` — pricing corrente EU
- `site:dcrainmaker.com [modello] review` — il più affidabile per test approfonditi

---

### Fitness band cinesi CrossFit/salute (budget ≤200€) — confronto Huawei/Xiaomi/Honor/JCVital/Hume — aggiornamento giugno 2026 (v2)

**Modelli verificati (shortlist CrossFit + HRV + SpO2 + VO2max + iOS):**
- Huawei Band 11 Pro (~59-75€) — GPS built-in GNSS, 1.62" AMOLED 2000nit, 18g, 5ATM, 8-14gg batteria, HRV overnight (non confermato come 24/7 continuo dalla scheda ufficiale), TruSeen 5.5+ non confermato (solo "optical HR sensor"), NO VO2max confermato, iOS sì (iOS 13+), HealthKit sync tramite Huawei Health app (confermato per Band 9, probabile per 11 Pro)
- Xiaomi Smart Band 10 Pro (~75€ idealo) — GPS 5 sistemi GNSS, 1.74" AMOLED 2000nit 60Hz, 21.6g, 5ATM, 15-21gg batteria, HRV sleep only (confermato "sleep HRV" nella spec ufficiale), NO VO2max confermato, iOS 13+ sì, Apple Health sync confermato (annuncio "Apple ecosystem support"), prezzo IT ~75€ (idealo giugno 2026). Disponibile globale giugno-agosto 2026.
- JCVital Pro V8 ECG (~199$/~185€ solo sito ufficiale) — screenless, ECG (4 categorie classificazione), HRV continuo 24/7, SpO2 continuo, IP68, batteria 15+ giorni, VO2max sì, NO recensioni indipendenti trovate (solo marketing interno). Venduto solo su jcvital.com. NO distribuzione EU/Amazon. Marca sconosciuta, zero test terzi.
- Hume Band 2.0 (~199-249$ solo sito ufficiale USA) — screenless, 8.6g, 5 LED 4 PD sensori, HRV continuo confermato, SpO2 continuo, iOS sì, Apple Health sì, raw data export sì, NO VO2max confermato, IP68, batteria 14gg. Distribuzione solo USA/UK, NO Italia/EU. Prezzo ~199-249$ (~185-230€) + spedizione internazionale.
- Huawei Band 9 (~28-37€ idealo) — 1.47" AMOLED, 14g, 5ATM, TruSeen 5.5 confermato, HRV (metodo non specificato nella spec, probabilmente overnight), SpO2 automatico, VO2max confermato nei workout, iOS sì HealthKit sync sì, NO GPS. Prezzo IT molto competitivo.
- Honor Band 9 (~28€ Amazon IT) — 1.56" AMOLED, 14g, 5ATM, NO GPS built-in (connected only), HR accuracy problems (5-10bpm higher in test indipendenti), NO VO2max confermato nelle spec, HRV non menzionato nelle spec ufficiali né nella recensione, iOS sì ma HealthKit subscription required (€2.99/mese per auto-push). Budget entry point.

**Note critiche per brand cinesi:**

**HRV "continuo 24/7" vs "overnight" — distinzione fondamentale:**
- Huawei marketing usa "24/7 HRV monitoring" ma le review mostrano che si riferisce a HRV durante il sonno per recovery score, non campionamento ogni minuto durante il giorno.
- Xiaomi Band 10 Pro dichiara esplicitamente "average HRV tracking during sleep" — overnight only, non continuo diurno.
- Solo WHOOP 5.0 fa HRV davvero continuo (ogni minuto, 24h). Nessuna fitness band sotto €200 raggiunge questo livello.

**VO2max — stato per ogni prodotto:**
- Huawei Band 9: confermato (RAI + VO2max nel tracking workout su support.huawei.com)
- Huawei Band 11 Pro: NON confermato nelle spec ufficiali o recensioni. Probabilmente assente.
- Xiaomi Band 10 Pro: NON confermato. Nessuna fonte lo menziona.
- JCVital V8: sì dichiarato, ma nessun test indipendente disponibile.
- Hume Band 2.0: NON confermato. App focalizzata su longevità/metabolismo, non sport performance.
- Honor Band 9: NON confermato.

**Distribuzione EU — problema critico per JCVital e Hume Band:**
- JCVital V8: nessun rivenditore EU trovato, solo sito jcvital.com con prezzi USD. Spedizione da Cina, dazi EU applicabili (~20%).
- Hume Band 2.0: distribuzione solo USA/UK. Per EU spedizione internazionale ~$30+ + eventuale IVA import.

**Honor HealthKit iOS — barriera nascosta:**
- Honor Health app su iOS non fa HealthKit push automatico senza abbonamento "Honor Health Connect" ($2.99/mese). Dati esportabili manualmente come CSV.

**GPS accuracy nei wristband cinesi:**
- Huawei Band 11 Pro: GPS built-in GNSS confermato, accuracy "adeguata per uso casual", deviazioni di rotta rilevate in test. Non per sport ad alta intensità.
- Xiaomi Band 10 Pro: GPS 5 sistemi (GPS+GLONASS+BeiDou+Galileo+QZSS) — spec più completa del gruppo. Non ancora testato in modo indipendente (lancio giugno 2026).
- Huawei Band 9, Honor Band 9: NO GPS built-in, connected only.

**Prezzi IT aggiornati (giugno 2026):**
- Huawei Band 11 Pro: ~59-75€ (idealo/Amazon IT)
- Xiaomi Smart Band 10 Pro: ~75€ (idealo, disponibilità giugno-agosto 2026)
- Huawei Band 9: ~28-37€ (idealo/Amazon IT)
- Honor Band 9: ~28€ (Amazon IT)
- JCVital Pro V8: $199 (~185€) solo sito ufficiale, spedizione da Cina
- Hume Band 2.0: $199-249 (~185-230€) solo USA/UK, no EU diretto

**Fonti affidabili per questa categoria:**
- consumer.huawei.com/en/wearables/[modello]/specs/ — spec ufficiali Huawei, direttamente leggibili
- mi.com/global/product/[modello]/ — spec ufficiali Xiaomi, HRV sleep-only esplicitato
- honor.com/global/wearables/[modello]/spec/ — struttura carica JS, non leggibile via WebFetch
- techadvisor.com — recensioni Honor Band 9 con test HR accuracy, molto affidabile
- gadgetpilipinas.net — review Huawei Band 11 Pro con sensori e GPS
- wearablesarena.com — review Huawei Band 11 Pro con dettagli batteria e GPS
- idealo.it — prezzi IT aggiornati

**Fonti problematiche:**
- humehealth.com — Shopify JS-heavy, nessuna spec leggibile via WebFetch
- jcvital.com/products/[modello] — Shopify JS-heavy, nessuna spec leggibile via WebFetch
- honor.com/global/wearables/[modello]/spec/ — HTML structure senza valori reali
- wareable.com — HTTP 403 su WebFetch

**Assenza totale di recensioni indipendenti per JCVital V8:**
- Zero risultati su dcrainmaker, wareable, pcmag, techradar, notebookcheck.
- Tutti i contenuti online sono marketing JCVital stesso o blog SEO che copiano i claim del produttore.
- BANDIERA ROSSA: nessun test accuracy ECG, HRV, SpO2 da fonte terza.

**Pattern di ricerca efficaci per questa categoria:**
- `"[modello] HRV sleep only OR continuous 24h confirmed"` — distingue HRV overnight da continuo
- `"[modello] VO2max confirmed specifications site:mi.com OR site:consumer.huawei.com"` — verifica VO2max ufficiale
- `"[modello] iOS HealthKit native OR subscription required"` — barriera Honor nascosta
- `"[brand] independent review dcrainmaker OR wareable OR pcmag"` — zero risultati per JCVital = bandiera rossa
- `"[modello] prezzo idealo Italia [anno]"` — prezzi IT aggiornati

**Aggiornamenti v2 (giugno 2026 — shortlist CrossFit):**

**Huawei Band 11 Pro (2026):**
- GPS built-in confermato (TechRadar, TechAdvisor, GizChina 2026) — £69.99/€74.90 lancio UK marzo 2026
- "TruSeen 6.0" NON compare nelle spec ufficiali consumer.huawei.com — probabilmente claim affiliati/blogger. Il sensore è unnamed nelle spec ufficiali.
- VO2max confermato via Huawei Support (training load + running ability index). MA: richiede attività outdoor (corsa, cammino, bici) — non disponibile su HIIT/lifting CrossFit.
- HRV: overnight/sleep (malgrado marketing "all-day"). Stesso pattern di tutti i Huawei Band.
- Batteria: 14gg dichiarati, 8gg uso tipico (dato ufficiale). Con GPS scende a ~2-4gg.
- Bluetooth 6.0 (più recente del Band 9 che usa BT 5.0).

**Xiaomi Smart Band 10 Pro (2026):**
- Lancio Cina maggio 2026, globale previsto giu-ago 2026.
- HRV sleep-only dichiarato esplicitamente da mi.com.
- VO2max: NON confermato in nessuna spec ufficiale né review al giugno 2026.
- Apple Health sync: confermato ufficialmente (primo Band a supportarlo). Non ancora testato in produzione da reviewer.
- SpO2: manuale ogni 10 minuti (più onesto di Huawei che dice "continuo").
- GPS 5 sistemi (GPS+GLONASS+BeiDou+Galileo+QZSS) — la spec GPS più completa del gruppo.
- HR accuracy "98,2%" claim produttore, non verificato indipendentemente.
- Dati locked in Mi Fitness — no raw export.

**JCVital Pro V8 ECG:**
- CONFERMA ASSOLUTA: zero review indipendenti su dcrainmaker, wareable, pcmag, techradar, notebookcheck.
- Produttore: jointcorp.com (ODM/OEM factory cinese). JCVital è brand di lancio.
- Distribuzione EU assente. Prezzo USD con dazi EU ~20% → reale ~240€.
- "Medical-grade ECG" non verificabile. Nessuna certificazione CE MDR 2017/745 trovata.
- Batteria 7gg — inferiore a Hume Band 2.0 (14gg) con sensori comparabili.
- Score: 2/10 — NON raccomandabile.

**Hume Band 2.0:**
- HRV 24/7 continuo confermato (Wareable, healnourishgrow, wellnesspulse). Valori coerenti con Oura/WHOOP come trend, non come assoluti.
- Raw data export confermato: Apple Health + Google Fit + Garmin + Fitbit + CSV export. Unico del gruppo con vera apertura dati.
- SpO2: NON menzionato nelle spec ufficiali del sito. Probabilmente assente come metrica separata.
- VO2max: non confermato. App focalizzata su longevità/recovery non sport performance.
- No GPS, no sport modes strutturati — non adatto per training tracking CrossFit.
- Distribuzione: worldwide ma sede USA. Nessun supporto EU locale. IVA import per EU.
- Prezzo $249 (~230€) — supera budget 200€ di ~30€.
- Peso 8,6g — il più leggero del gruppo, ottimo per CrossFit (non disturba durante lifts).
- Score: 7,8/10 per utenti orientati a recovery/longevità con API aperta.

**Honor Band 9 — aggiornamento:**
- iOS HealthKit tecnicamente supportato ma sync incompleto: SpO2 e workout minutes non sempre pushati automaticamente (user reports Apple Community).
- HR accuracy: 5-10bpm superiore durante esercizio (techadvisor test).
- VO2max: non confermato.
- Rispetto a Huawei Band 9 allo stesso prezzo (€35): inferiore su tutti i parametri. Difficile da raccomandare.

**Fonti affidabili aggiunte (fitness band cinesi v2):**
- gadgetsandwearables.com/2026 — Xiaomi Band 10 Pro review, HR accuracy test vs chest strap
- the-gadgeteer.com — specs Xiaomi Band 10 Pro lancio, HRV sleep confermato
- trustedreviews.com — Xiaomi Band 10 Pro review (HR accuracy, HIIT limitations)
- healnourishgrow.com — Hume Band 2.0 review con raw data export confermato
- myreviewabout.com — Hume Band 2.0 specs: 5 LED + 4 PD, 1.400 data points/day
- smartwatchspecifications.com — Huawei Band 11 Pro GPS built-in confermato
- gizguide.com — Huawei Band 11 Pro review (VO2max confermato, TruSeen unnamed)
- huawei support content/en-us00736792 — VO2max/training load confermato per Band series

**Fonti problematiche aggiunte:**
- gizmochina.com — HTTP 403 su WebFetch
- gizguide.com — JS-heavy, body articolo non estraibile via WebFetch
- wareable.com — HTTP 403 su WebFetch (confermato anche per Hume Band 2.0)
- wellnesspulse.com — HTTP 403 su WebFetch
- healnourishgrow.com — accessibile via WebFetch (funziona)
- jointcorp.com — HTTP 403 su WebFetch

---

### Fitness tracker / Smart band con sensori avanzati (budget ≤200€) — aggiornamento giugno 2026

**Modelli verificati:**
- Fitbit Charge 6 (~130-160€) — built-in GPS, AMOLED 1.04", 15g senza strap, 5ATM, 7 giorni batteria
- Garmin Vivosmart 5 (~100-130€) — connected GPS (no built-in), 24.5g, 5ATM, 7 giorni, OLED 10.5×18.5mm
- Amazfit Band 7 (~40-55€) — no GPS built-in (connected), 28g, 5ATM, 18 giorni, AMOLED 1.47"
- Xiaomi Smart Band 9 Pro (~60-80€) — built-in GPS (5 sistemi), 24.5g, 5ATM, 21 giorni, AMOLED 1.74"
- Samsung Galaxy Fit 3 (~50-65€) — connected GPS, 18.5g, 5ATM + IP68, 13 giorni, AMOLED 1.6"
- Huawei Band 9 (~40-60€) — no GPS, 14g, 5ATM, 14 giorni, AMOLED 1.47"

**Note critiche per categoria fitness tracker:**

**HRV — distinzione fondamentale:**
- HRV "continuo" vero (campionamento ogni minuto o più frequente, 24h): nessun modello in questa fascia di prezzo. Tutti fanno HRV durante il sonno o su richiesta.
- Fitbit Charge 6: HRV solo notturno (durante sonno ≥3h). NESSUNA misurazione diurna continua.
- Garmin Vivosmart 5: HRV raccolto durante il sonno per Body Battery e stress; nessun HRV Status separato (feature riservata a Garmin mid/high). Dati usati internamente, non esposti come metrica diretta.
- Amazfit Band 7: HRV usato per stress RMSSD, non esposto come valore separato al'utente.
- Xiaomi Band 9 Pro: HRV non disponibile come metrica esplicita.
- Huawei Band 9: HRV presente ma non continuo diurno.

**VO2max:**
- Garmin Vivosmart 5: confermato (richiede attività con cardio ≥15 min).
- Fitbit Charge 6: confermato come "Cardio Fitness Score" (stima, non clinica).
- Amazfit Band 7: NON confermato nelle spec ufficiali.
- Xiaomi Band 9 Pro: confermato (Training Load, VO2max nella sezione sport).
- Samsung Galaxy Fit 3: non confermato nelle spec ufficiali Samsung.
- Huawei Band 9: confermato (con avvertenza: non visibile durante workout outdoor su alcuni modelli).

**iOS e HealthKit:**
- Fitbit Charge 6: iOS sì, HealthKit NATIVO NO — solo tramite app terze parti a pagamento.
- Garmin Vivosmart 5: iOS sì, HealthKit sì via Garmin Connect (post-2020 tutti i Garmin).
- Amazfit Band 7: iOS sì, HealthKit sì via Zepp app (sync confermato).
- Xiaomi Band 9 Pro: iOS sì (≥12), HealthKit sì via Mi Fitness (permesso da abilitare).
- Samsung Galaxy Fit 3: SOLO ANDROID. Non funziona con iPhone. Eliminato dalla selezione iOS.
- Huawei Band 9: iOS sì (≥13), HealthKit sì via Huawei Health app (sync confermato).

**CrossFit/HIIT come profilo sport:**
- Garmin Vivosmart 5: HIIT confermato tra i 14 profili.
- Amazfit Band 7: 120 sport mode, HIIT presumibilmente presente (non nominato esplicitamente).
- Xiaomi Band 9 Pro: 150+ profili, HIIT presente.
- Fitbit Charge 6: 40 profili, HIIT presente tra le attività.
- Huawei Band 9: 100+ profili, HIIT confermato.
- Samsung Galaxy Fit 3: 100+ profili, HIIT presumibilmente presente.

**Fonti affidabili per fitness tracker:**
- wiki.garminrumors.com — specifiche Garmin complete, sensori, sport profiles
- consumer.huawei.com/en/wearables/[modello]/specs/ — specifiche ufficiali Huawei, direttamente leggibili
- mi.com/global/product/[modello]/specs/ — specifiche ufficiali Xiaomi, direttamente leggibili
- samsung.com/us/support/answer/ANS10004550/ — specs Galaxy Fit 3 (limitato, non ha HRV/VO2max esplicitato)
- dcrainmaker.com — recensioni con dettaglio tecnico su GPS accuracy, HRV, SpO2 metodi
- notebookcheck.net — recensioni dettagliate Amazfit con analisi accuracy
- forums.garmin.com — conferme su funzionalità limitate Vivosmart 5 (HRV Status non disponibile)
- community.fitbit.com — conferme su assenza HealthKit nativo Fitbit

**Fonti problematiche per fitness tracker:**
- store.google.com/fitbit_charge_6_specs — redirect cookie consent, non accessibile via WebFetch
- us.amazfit.com/products/amazfit-band-7 — restituisce solo JS (Shopify), nessun dato leggibile
- versus.com — HTTP 403 su WebFetch diretto
- wareable.com — HTTP 403 su WebFetch diretto
- gadgetsandwearables.com — restituisce struttura HTML senza body articolo

**Pattern di ricerca efficaci per fitness tracker:**
- `"[modello] HRV continuous daytime or sleep only"` — distingue HRV continuo da notturno
- `"[modello] HealthKit iOS sync confirmed"` — verifica integrazione nativa vs terze parti
- `"[modello] VO2max confirmed specifications"` — verifica se è feature effettiva o solo marketing
- `site:wiki.garminrumors.com [modello]` — spec Garmin complete
- `site:consumer.huawei.com [modello] specs` — spec ufficiali Huawei
- `site:dcrainmaker.com [modello] review` — profondità tecnica GPS, sensori, accuracy
