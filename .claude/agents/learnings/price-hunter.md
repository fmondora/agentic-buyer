# PriceHunter — Learnings

## REGOLA CRITICA — Prezzi da comparatori, MAI da articoli

**ERRORE COMMESSO**: nella prima ricerca TV 55", il prezzo Sony BRAVIA 3 55" e stato preso da un articolo di SpazioGames/Tom's Hardware di marzo 2026 che riportava un'offerta Amazon a €614. Il prezzo reale a giugno 2026 e €699-720 (K55S35B) o €529 (K55S39B). L'utente ha trovato prezzi completamente diversi.

**REGOLA**: usare SOLO prezzi da comparatori live (idealo.it, trovaprezzi.it) o pagine prodotto e-commerce. Gli articoli di blog riportano offerte a tempo che scadono. Ogni prezzo deve avere il link diretto alla pagina dove e visibile ORA.

## Fonti affidabili

- **idealo.it** (via WebSearch `site:idealo.it [modello]`) — FONTE PRIMARIA per prezzi attuali. Snippet mostra prezzo minimo aggiornato. Link diretto alla pagina confronto prezzi.
- **trovaprezzi.it** (via WebSearch `site:trovaprezzi.it [modello]`) — FONTE PRIMARIA alternativa. Snippet mostra prezzo minimo.
- **MediaWorld.it** — WebFetch funziona bene, restituisce prezzi strutturati con spedizione e disponibilità. Link diretto alla pagina prodotto.
- **Unieuro.it** — pagine prodotto con prezzo, ma WebFetch restituisce solo framework Angular. Usare WebSearch per prezzo da snippet.
- **WebSearch su siti tech specializzati** (tuttoandroid.net, tomshw.it, hwupgrade.it) — ATTENZIONE: utili per scoprire modelli e confronti, ma i PREZZI citati possono essere promo scadute. Sempre verificare su idealo/trovaprezzi prima di riportarli.
- **occhioaiprezzi.com** — comparatore leggero, mostra la data ultimo aggiornamento, buon fallback quando idealo blocca
- **Kitele.com** — schede prodotto TV con prezzi storici cross-country, utile per Philips e modelli meno diffusi

## Fonti problematiche

- **trovaprezzi.it (WebFetch)** — restituisce 403 sistematicamente; usare WebSearch con site:trovaprezzi.it oppure cercare la scheda prodotto specifica
- **idealo.it (WebFetch)** — restituisce 503 sistematicamente; usare WebSearch con site:idealo.it per ottenere prezzi dai snippet
- **amazon.it / amazon.de (WebFetch)** — blocca con CAPTCHA o restituisce solo JS minificato; usare WebSearch per trovare articoli di terzi con prezzi
- **unieuro.it (WebFetch)** — restituisce solo CSS/framework Angular, nessun dato prodotto
- **ebay.it (WebFetch diretto su listing)** — restituisce 403; meglio WebSearch per trovare prezzi

## Pattern di ricerca efficaci

Per TV 55 pollici:
- `"[modello]" prezzo amazon.it [anno]` — trova articoli tech con prezzi esatti
- `"[modello]" a € [sito:idealo.it]` — snippet con prezzo minimo diretto
- `TV 55 pollici sotto 400 euro amazon [anno] migliore` — confronto budget con raccomandazioni
- `site:tuttoandroid.net OR site:tomshw.it "[modello]" amazon [anno]` — articoli offerta affidabili
- Usare l'anno corrente nella query aumenta la rilevanza dei risultati

## Note per categoria

### Fitness tracker / Smart band (aggiornato giugno 2026)

**Modelli esistenti nel catalogo 2026:**
- Amazfit Band 9: NON ESISTE. La serie Amazfit Band si ferma alla Band 7 (lanciata 2022). Non cercare questo modello.
- Amazfit Helio Strap (2025): tracker senza display, €99.91 amazon.it (ASIN B0F8HJCB47). Stesso prezzo su amazon.de/fr/es (€99.90). Sito ufficiale esaurito. idealo.it da €98.99 (17 offerte).
- Fitbit Charge 6 (2023): ASIN amazon.it è B0CHN3W617 (NON B0CZGP1H8K che dà 404). Prezzo €84.90 amazon.it. idealo.it da €84.90. MediaWorld €129.29 (prezzo pieno).
- Fitbit Air (2026): ASIN B0GS7D8BN9. Prezzo €99.99 su tutti Amazon EU (it/de/fr/es). idealo.it da €99.99 (storico: min €99.99, max €144.98). idealo.de/at €99.00.
- Garmin Vivosmart 5 (2022, ancora in produzione): successore (Vivosmart 6) NON ancora disponibile a giugno 2026.
- Garmin Vivosmart 6: leak da CES 2026, lancio atteso maggio-giugno 2026 ma non ancora ufficiale a giugno 2026. Prezzo stimato $150-180 USD (~€140-170). NON cercare perché non venduto.
- Xiaomi Smart Band 9 (2024) e Smart Band 9 Pro (2024) — successore: Smart Band 10 Pro (2026)
- Samsung Galaxy Fit 3 (2024, ancora in produzione)
- Huawei Band 9 (2024) e Band 8 (2023, modello precedente scontato)
- WHOOP: dal 2025 WHOOP 5.0 ha sostituito il 4.0. Abbonamento obbligatorio, device non funziona senza.

**WHOOP struttura prezzi 2025-2026 (aggiornato giugno 2026):**
- Piano One: €199/anno — include WHOOP 5.0, sensori base (sonno, sforzo, recupero, VO2max, HRV), AI coaching
- Piano Peak: €264/anno — aggiunge Healthspan (età fisiologica), stress, approfondimenti salute
- Piano Life: €399/anno — include WHOOP MG (medical grade), ECG, rilevamento aritmie, pressione
- Tutti i piani: abbonamento annuale obbligatorio. Mensile non disponibile (solo dopo 12 mesi iniziali).
- Test in Italia (da maggio 2026): device separato €69 + abbonamento €199/anno = €268 primo anno
- Costo pluriennale: anno 1 = €199 (device incluso standard), anno 2+ = €199/anno (stesso piano)
- ASIN amazon.it B0DY2VVZWZ = piano One 12 mesi, €199, stesso prezzo su DE/FR/ES

**Sensori avanzati (HRV, VO2max) — chi ce li ha davvero:**
- HRV vero: Fitbit Charge 6 (ECG + HRV), Garmin Vivosmart 5 (Body Battery basata su HRV), WHOOP 5.0 (HRV continuo 24/7), Amazfit Helio Strap (HRV continuo)
- VO2max: Fitbit Charge 6 (stima via GPS), Garmin Vivosmart 5 (con camminata 15 min), WHOOP 5.0, Amazfit Helio Strap
- SpO2: tutti i modelli sopra + Xiaomi Smart Band 9 Pro, Samsung Galaxy Fit 3, Huawei Band 9
- Fitbit Air: HRV SI (continuo), VO2max SI, SpO2 SI — successore Charge 6 senza display
- Amazfit Helio Strap: HRV SI, VO2max SI, SpO2 SI — senza display, no subscription
- Xiaomi Smart Band 9 (base): NO HRV, NO VO2max — solo SpO2 e HR di base
- Samsung Galaxy Fit 3: NO HRV, NO VO2max, ha SpO2 e monitoraggio sonno
- Huawei Band 9/8: NO HRV, NO VO2max, SpO2 presente, TruSleep avanzato

**Fascia prezzi live (giugno 2026, Amazon.it via scraper):**
- Amazfit Band 7: €20.99 amazon.it (modello 2022, quasi fine vita, MA senza HRV/VO2max veri)
- Amazfit Band 7 amazon.de: €6.99 (ANOMALO — venditore marketplace, stock residuo, non affidabile)
- Amazfit Helio Strap: €99.91 amazon.it / €99.90 amazon.de/fr/es / ~€98.99 idealo.it
- Samsung Galaxy Fit 3: €41.90 amazon.it / €41.99 MediaWorld
- Huawei Band 9: €35.38 amazon.it / €29.80 amazon.de (BEST EU price)
- Huawei Band 8 (precedente): ~€29.90 idealo / €59 amazon.it (versione ES — attenzione)
- Xiaomi Smart Band 9: ~€29.99 idealo / €45.18 amazon.it (Glacier Silver)
- Xiaomi Smart Band 9 Pro: €48.49 amazon.it / €41.23 amazon.es (BEST EU price)
- Fitbit Charge 6: €84.90 amazon.it (ASIN B0CHN3W617) / €85.00 amazon.de / idealo.it da €84.90 / MediaWorld €129.29
- Fitbit Air: €99.99 amazon.it (ASIN B0GS7D8BN9) / €99.99 amazon.de/fr/es / idealo.it €99.99 / idealo.de €99.00
- Garmin Vivosmart 5: €132.49 amazon.it / €122.57 amazon.de (risparmio ~€10 su DE) / idealo.it da €130.68
- WHOOP 5.0 abbonamento One: €199/anno amazon.it (device incluso nel piano standard; in IT test vendita separata: device €69 + €199/anno)
- Fitbit Charge 5 (precedente): €98.49 amazon.it MA solo usato seconda mano — fuori produzione

**ASIN corretti fitness tracker (verificati giugno 2026):**
- Amazfit Helio Strap: B0F8HJCB47 (funziona su IT/DE/FR/ES)
- Fitbit Air: B0GS7D8BN9 (funziona su IT/DE/FR/ES)
- WHOOP 5.0 One Annual: B0DY2VVZWZ (funziona su IT/DE/FR/ES)
- Fitbit Charge 6 (amazon.it): B0CHN3W617 — ATTENZIONE: B0CZGP1H8K dà 404, non usarlo
- Fitbit Charge 6 idealo.it ID: 203291761

**Fonte WHOOP:** abbonamento su amazon.it (ASIN B0DY2VVZWZ) = €199/anno piano One. Il device è incluso nell'abbonamento nel piano standard. In Italia test di vendita separata (device €69 + abb. €199). Verificare sul sito WHOOP per struttura attuale.

**Amazfit Band 7 (€6.99 amazon.de)**: prezzo sospetto, sicuramente venditore third-party con stock residuo. Non riportare come prezzo affidabile. Usare €20.99 amazon.it come riferimento.

**Smart band cinesi 2026 (Huawei Band 11 Pro, Xiaomi Band 10 Pro, Honor Band 9) — note operative (aggiornato giugno 2026 — 6.18 sale):**
- Huawei Band 11 Pro (2026): ASIN B0GGHRJR23, €59.90 amazon.it (confermato scraper), €54.90 amazon.de (BEST EU), €45.37 amazon.es (MIN EU — confermato scraper 6/2026), idealo.it €59.90 (min storico €56.43), idealo.de/at €54.90. Listino ufficiale €74.90. AliExpress stima CN ~€38 IOSS incluso (non verificabile direttamente). Risparmio reale AliExpress CN vs amazon.es: ~€7 — NON vale il rischio/attesa.
- Xiaomi Smart Band 10 Pro (2026): ASIN B0GQ3FYM27 (Nero, €79.99 amazon.it), amazon.es €66.10 (BEST EU — confermato scraper), amazon.de/fr €75.99. idealo.it €75.41 (min storico €75.41). Listino €79.90 (alluminio) / €99.90 (NFC ceramica). AliExpress stima CN ~€52. Risparmio CN vs amazon.es: ~€14 — marginale per prodotto appena uscito.
- Honor Band 9 (2024): ASIN B0CX8774TW, amazon.de €26.00 (BEST EU — confermato scraper 6/2026), amazon.it €40.41, amazon.es €39.99, amazon.fr €59. idealo.it snapshot €29.25 (marketplace) ma scraper mostra €105 (anomalo). AliExpress stima CN ~€17. Risparmio vs amazon.de: ~€9 — amazon.de già convenientissimo, AliExpress NON conveniente.
- Huawei Band 9 (2024): ASIN B0CYCDKR2S = colori diversi per paese (Blue IT, Lemon Yellow DE). amazon.de €39.90 (confermato scraper), amazon.it €69.00 (versione Blue — prezzo alto), amazon.fr/es €69. idealo.it scraper €44.90 (min storico €24.88). AliExpress stima CN ~€20. Risparmio vs amazon.de: ~€20 — ma amazon.de già a €39.90 è ragionevole.
- AliExpress per band cinesi: SISTEMATICAMENTE blocca WebFetch con JS/CAPTCHA. Usare WebSearch per stime, ma prezzi AliExpress non verificabili direttamente. Per prodotti Huawei/Xiaomi/Honor, il prezzo EU (amazon.es/de/idealo) è spesso comparabile o inferiore rispetto ad AliExpress + rischi (garanzia, reso, tempi).
- JCVital Pro V8 ECG: $199 USD (~€172 a tasso 1.16). Spedizione globale gratuita (sito Singapore). Acquisto diretto da jcvital.com: IVA 22% alla dogana italiana (~€38) + handling corriere €12 = costo reale ~€221. No subscription. Sito WebFetch funziona su /products/jcvital-v8-ecg-smart-band. NON disponibile su Amazon EU / idealo EU. Prodotto di nicchia senza equivalente EU.
- Hume Band 2.0: $249 USD sito (~€215). Coupon MYREVIEWABOUT: -20% → $199.2 (~€172). Spedizione gratuita worldwide. USA → Italia: IVA 22% alla dogana + handling €12 = costo totale €221 (con coupon) o €274 (senza). Codici alternativi da siti affidabili: WRBL20 (-20%), blackcooltz25 (-25%), LHEALTH20 (-20%). Sito hume.health: ECONNREFUSED su WebFetch — inutilizzabile. myreviewabout.com e wareable.com hanno dettagli prezzo (wareable.com dà 403).
- AliExpress 6.18 Mid-Year Sale (15-20 giugno 2026): coupon attivi fino al 30/6 — USTK8S (-€8 su min €49), USTK18S (-€18 su min €99). I coupon summerr con codici ITSS sono scaduti il 10/6.
- Tasso cambio EUR/USD giugno 2026: 1 EUR = 1.16 USD (quindi $100 = ~€86).

### Tavole e pannelli in larice 200x80cm 18mm (aggiornato giugno 2026)

**Realta del mercato**: la dimensione 200x80cm con spessore 18mm NON esiste in larice massello nel mercato mass-market italiano. Leroy Merlin e Tecnomat vendono quella misura in ABETE lamellare, non larice. Il larice viene venduto in tavole piu strette (90-150mm larghezza) o in formati su misura da falegnami.

**Prodotti larice realmente acquistabili online:**
- Leroy Merlin: listone larice grezzo 200x15cm sp.20mm (cod.35254765): ~€49.48/pz — link: https://www.leroymerlin.it/prodotti/falegnameria/legno-da-costruzione-battiscopa-e-listelli/perline-e-listoni/listone-larice-grezzo-naturale-1-scelta-l-200-x-h-15-cm-sp-20-mm-35254765.html
- Leroy Merlin: listone larice clip esterno 200x12cm sp.21mm (cod.35187530): ~€10.90/pz o €45/m² — link: https://www.leroymerlin.it/prodotti/listone-con-fissaggio-a-clip-in-legno-larice-naturale-l-200-x-l-12-cm-x-sp-21-mm-35187530.html
- Pellet Legnami Brenta: tavola larice siberiano 20x90x2000mm AB: €7.30/pz — in stock — link: https://pellet-legnami.it/products/tavole-per-recinzione-20x90x2000-ab-larice-siberiano
- Pellet Legnami Brenta: tavola larice siberiano 28x140x2000mm BC: €11.18/pz — in stock — link: https://pellet-legnami.it/products/doghe-da-esterno-28x140x2000mm-bc-larice-siberiano
- Pellet Legnami Brenta: perlina larice siberiano 26x145x4000mm B: €20.50/pz — link: https://pellet-legnami.it/products/perline-legno-26x145x4000mm-b-larice-siberiano
- Putzer: tavola larice piallata 24x190x2000mm: €19.00/pz — link: https://putzer.com/it/Tavole-In-Larice-Piallate-Sui-4-Lati-Dim-24-X-190-X-2000-Mm
- Putzer: pannello 3 strati larice 19mm B/C (formato 5000x2050mm): €98.00 (foglio intero) — link: https://putzer.com/it/Pannello-3-Strati-In-Larice-19-Mm-B/C

**Alternativa abete lamellare 200x80x18mm (se accettata):**
- Leroy Merlin: tavola lamellare abete 200x80 sp.18mm (Cardigliano Legnami): €72.64/pz — link: https://www.leroymerlin.it/prodotti/falegnameria/tavole-pannelli-in-legno-e-cavalletti/tavole-in-legno/legno-lamellare/tavola-legno-lamellare-abete-200-x-80-cm-sp-18-mm-36332821.html
- Leroy Merlin: tavola lamellare abete 200x80 sp.18mm (1a scelta): ~€39.90-40.49/pz

**Fonti che funzionano bene per questa categoria:**
- pellet-legnami.it: WebFetch funziona perfettamente, prezzi esatti, stock indicato
- putzer.com: snippet WebSearch mostrano prezzi, WebFetch restituisce solo JS
- leroymerlin.it: snippet WebSearch mostrano prezzi, WebFetch restituisce 403

**Fonti problematiche per questa categoria:**
- tecnomat.it: WebFetch 403, snippet non mostrano prezzi esatti
- manomano.it: 403 sistematico
- leroymerlin.it: 403 sistematico su WebFetch — usare solo snippet WebSearch
- wood4you.it: sito in manutenzione a giugno 2026
- bricolegnostore.it: prodotti larice solo in larghezze strette (100-150mm), nessun 80cm

**Note operative:**
- Per rivestimento parete 80cm: usare piu tavole da 200x14-19cm affiancate (5-6 tavole per coprire 80cm di larghezza), non una tavola unica da 80cm
- Il pannello 3 strati larice (ilmiopezzo.com, putzer, derve.it) puo essere tagliato su misura 200x80 a ~€83.63/m2, quindi ~€53.5 per 0.64m2

### Ombrelloni da deck/giardino palo laterale 3.5m (aggiornato giugno 2026)

**Realtà del mercato**: il requisito "3.5m+ palo laterale, rotante 360°, inclinabile, base zavorrabile" divide il mercato in tre fasce nette:

**Fascia consumer (80-260€) — qualità bassa, montagna sconsigliata:**
- tectake 3.5x3.5 braccio 360° (ASIN B0GX1P8C7R): €85.79 amazon.it — palo sottile, base a croce in acciaio inclusa. Solo per uso leggero.
- tectake 3.5x3.5 braccio 360° con LED (ASIN B0GWQX3221/B0GWQLMTGC): €99.79 amazon.it
- IDMarket AJACCIO Ø350 360°: €119.99 idmarket.it — 24kg, base lastre acqua incluse, 4 pannelli separati
- Briconess Premium Ø350 360° inclinabile: €258.90 briconess.com — palo 50x67mm alluminio, 23kg, base non inclusa
- BAKAJI 3x3 360° (ASIN B07QCSV27W): €199 amazon.it — è 3x3 non 3.5x3.5, valutare

**Fascia media (600-900€) — qualità accettabile per uso intensivo:**
- PiscineOnline.it braccio 350cm alluminio 60/84mm: €617.50 — palo robusto 60/84mm, 27kg, 360°+inclinabile, base NON inclusa (4 lastre 25kg cad.)
- Danieli Ombrellificio 3x3 braccio alluminio: €716 IVA incl. (danielihoreca.it) — solo preventivo per 3x3, non 3.5m. Retrattile, 360°+inclinabile, acrilico 300g/mq

**Fascia professionale (1.400€+) — qualità garantita per montagna:**
- Scolaro Palladio Braccio 3.5x3.5 (ombrapro.it): €1.650-1.750 + base €60-210 — alluminio 40kg, acrilico 5y garanzia
- Scolaro Leonardo Braccio 3.5x3.5 (designperte.it): ~€1.500+
- Ombrellificio Veneto "K" 3.5x3.5: €2.805 (designperte.it) — alto di gamma, gas spring, anodizzato
- Torino Braccio 350cm (beautifulgardenline.com): €1.140-1.242 — alluminio+iroko, base inclusa, 2y+5y garanzia

**Brand elencati dall'utente che NON esistono nel budget 500-700€:**
- Scolaro Mistral/Tosca: modelli non trovati nei cataloghi 2026 (probabilmente fuori produzione o nomi errati)
- Caravita Parasol: brand premium tedesco, prezzi a 9.500€+, non venduto in Italia retail
- Suns Penelope/Monaco: brand olandese, non trovato su canali IT (solo sito produttore)
- Fim Flexy: struttura modulare professionale da €3.800+
- Umbrosa Paraflex: misure max 270-300cm, non 350cm
- Doppler Protect/Active 370: €799 dopplershop.it (solo CH/AT), non disponibile su amazon.it/eBay.it

**Basi zavorrabile (separate) per braccio laterale:**
- Outsunny 4 pezzi 100x100cm 80kg acqua/120kg sabbia (ASIN B0CV5LJKPX): €72.95 amazon.it — in stock
- VOUNOT plastica 52L acqua/100kg sabbia (ASIN B08J29HFXY): €64 amazon.it — in stock

**Fonti affidabili per questa categoria:**
- piscineonline.it (WebFetch funziona, prezzi esatti, stock numerico indicato)
- idmarket.it (WebFetch funziona, prezzo esatto, scheda completa)
- briconess.com (WebFetch funziona)
- danielihoreca.it (WebFetch funziona, ma prezzi solo per ordini B2B: IVA esclusa)
- dopplershop.it (JS-heavy, WebFetch restituisce solo JS; una pagina prodotto diretta funziona)
- ombrapro.it (WebFetch funziona, prezzi esatti)

**Fonti problematiche per questa categoria:**
- manomano.it: 403 sistematico
- trovaprezzi.it: 403 su WebFetch; usare WebSearch site:
- idealo.it: 503 su WebFetch; usare WebSearch site:
- levanteshop.it/ombrelloni: lista parziale, prezzi per modelli grandi non mostrati

### TV 55 pollici (aggiornato giugno 2026)

**Fasce di prezzo tipiche:**
- Budget (<350€): TCL 55V6C (~242€), Haier H55K85FUX (~280€), TCL 55P6K (~280-299€), Hisense 55A6N (~322€)
- Mid-range (350-500€): Xiaomi A Pro 55 2026 (~329€), Hisense 55E79NQ (~357€), Samsung UE55DU7170 (~449€), LG QNED80 (~449€)
- Premium (>500€): Sony BRAVIA 3 K55S39B (~529€), LG 55QNED86A6 (~599€), Sony BRAVIA 3 K55S35B (~699€), Philips 55PUS8909 Ambilight (~789€)
- NOTA: Sony BRAVIA 3 ha 2 varianti 55" — K55S39B (€529) e K55S35B (€699). Il prezzo di €614 era una promo Amazon scaduta a marzo 2026.

**Fascia QLED 55" entry-mid (ricerca giugno 2026, budget 350-550€):**
- Hisense 55E7Q (base, QLED 144Hz 2025): ~€379 idealo
- Hisense 55E7Q PRO (QLED 144Hz 2025, Dolby Atmos, VIDAA U8): ~€399-449 (idealo €399, occhioaiprezzi €449 aggiornato 13/6/2026)
  - NOTA: occhioaiprezzi aggiornato OGGI mostra €449, idealo snippet ancora a €399 — proba offerta flash passata
- TCL 55C655 (QLED 2024): ~€404 idealo
- Samsung QE55Q70DAT (QLED 2024, 120Hz): ~€548 idealo / ~€549 trovaprezzi

**Fascia QLED/Mini-LED 55" mid-premium (500-800€, ottimi colori+audio):**
- Samsung QE55QN70FAUXZT (Neo QLED Mini LED 2025, 144Hz): €599 MediaWorld (spedizione gratuita, in stock)
  - Link diretto: https://www.mediaworld.it/it/product/_samsung-qe55qn70fauxzt-55--435470.html
- LG 55QNED86A6A (QNED evo AI 2025, 120Hz, Dolby Atmos): €556-599 (trovaprezzi/idealo)
  - Link idealo: https://www.idealo.it/confronta-prezzi/206188802/lg-55qned86a6.html
- TCL 55C7K (QD-Mini LED 2025, 144Hz, B&O audio, 3000 nit): ~€578-599 trovaprezzi / €539 idealo
  - Link idealo: https://www.idealo.it/confronta-prezzi/206289141/tcl-c7k.html (VERIFICARE taglia: questa voce potrebbe essere 50")
  - Link 55": https://www.idealo.it/confronta-prezzi/206292371/tcl-55c7k.html (€1003 — prezzo anomalo, verificare)
  - Su Amazon.it: https://www.amazon.it/TCL-55C7K-QD-Mini-CrystGlow-HVA-Panel/dp/B0F5BP4KFM
- Samsung QE55Q80DAT (QLED 2024, Dolby Atmos): €649 MediaWorld / €753 idealo
  - Link MediaWorld: https://www.mediaworld.it/it/product/_samsung-qe55q80datxzt-370688.html
- Hisense 55U7Q (QLED Mini LED, 2025): ~€466 idealo — 40W 2.1ch Dolby Atmos, 144Hz, Dolby Vision IQ
- Hisense U7Q Pro 55 (Mini LED, 2025): ~€549 idealo — 165Hz, Dolby Vision, Dolby Atmos
- Samsung QE55QN80F (Neo QLED Mini LED, 2025): €575-669 idealo / €679 MediaWorld / €799 Samsung.com
  - Samsung.com: soundbar B400F in regalo (promo fino 22/06/2026) + 5% con Gift Card (fino 30/06/2026)
- Philips 55PUS8919 The One Ambilight (LED, 2025): ~€599-674 idealo — ATTENZIONE: LED standard, non QLED
- Samsung TQ55QN85F (Neo QLED Mini LED, 2025): ~€646 idealo — più luminoso del QN80F, top Samsung budget
- Hisense 55U8Q (Mini-LED QLED 2025, 165Hz, 4.1.2 Dolby Atmos, eccellente audio): ~€746 idealo
  - Link Amazon: https://www.amazon.it/Hisense-Mini-LED-55U8Q-Octagonal-Multi-Channel/dp/B0F1WHZW4G
- TCL 55C7L (SQD-Mini LED QLED, 2026): ~€735 idealo — B&O audio, 2700 nit, 800 zone, 144Hz, Google TV
- TCL 55C8L (SQD-Mini LED QLED, 2026): ~€804 idealo — 3000 nit, 1008 zone, B&O audio, 144Hz, top TCL
- Samsung QE55QN85F 55 (Neo QLED, 2025): ~€646 idealo — fascia alta Samsung
- Sony Bravia 7 K55XR70 (Mini LED QLED, 2024): ~€1300+ EU — fuori budget 1000€

**Modelli con miglior audio integrato 55" (giugno 2026):**
1. TCL 55C7K / C7L / C8L — Bang & Olufsen (sistema audio certificato, il migliore della categoria)
2. Hisense 55U8Q — 4.1.2 Dolby Atmos (più canali audio integrati)
3. Samsung QE55QN70FAUXZT — OTS Lite + Dolby Atmos
4. Hisense 55E7Q PRO — Dolby Atmos (entry level, soddisfacente)

**Brand affidabili per qualità/prezzo:**
- TCL e Hisense dominano la fascia budget con Google TV o VIDAA, buone recensioni
- Xiaomi A Pro 2026 ha QLED nativo, ottimo per chi vuole qualità visiva a meno di 400€
- Samsung e LG restano riferimento mid-range; prezzi alti ma garanzia e assistenza eccellenti
- TCL C7L/C8L (2026) sono le migliori QLED Mini LED nel budget 700-900€ con B&O audio

**Fascia PREMIUM 55" OLED/QLED (ricerca giugno 2026, budget 1000-5000€):**

- Samsung S95F 55" (QE55S95FATXZT, QD-OLED 2025): ~€1.180-1.249 trovaprezzi/mediaworld — PREZZO OTTIMO rispetto al listino €2.499
  - Kelkoo giugno 2026 conferma prezzi in range €1.180-1.384
  - MediaWorld: €1.249,49 spedizione gratuita
  - Link trovaprezzi: https://www.trovaprezzi.it/televisori-lcd-plasma/prezzi-scheda-prodotto/samsung_s95f_55_qe55s95fatxzt-v
  - Link MediaWorld: https://www.mediaworld.it/it/product/_samsung-qe55s95fatxzt-55-oled-4k-435438.html
- Samsung S95D 55" (QE55S95DAT, QD-OLED 2024): €1.483 idealo / €1.788 MediaWorld (venditore terzo) — superato dal S95F più economico
  - Samsung.com: ESAURITO (non in vendita diretta)
  - Link idealo: https://www.idealo.it/confronta-prezzi/204173602/samsung-qe55s95dat.html
  - Link MediaWorld (venditore terzo): https://www.mediaworld.it/it/product/_samsung-gq55s95dat-tv-oled-piatto-55-oled-4k-144508458.html
- Samsung QN90F 55" (QE55QN90FAT, Neo QLED Mini LED 2025): ~€990-1.130 trovaprezzi/idealo
  - Samsung.com: ESAURITO. Promo soundbar B400F in regalo (3-22/6/2026)
  - Link trovaprezzi: https://www.trovaprezzi.it/televisori-lcd-plasma/prezzi-scheda-prodotto/samsung_qn90f_55_qe55qn90fatxzt-v
  - Link idealo: https://www.idealo.it/confronta-prezzi/206822535/samsung-qe-qn90fat.html
- Samsung QN95F 55": NON COMMERCIALIZZATO IN ITALIA — top Samsung 4K è QN90F
- LG OLED G5 55" (OLED55G54LW / OLED55G55LW 2025): €988-1.199 idealo/occhioaiprezzi
  - MediaWorld: €1.214,28 spedizione gratuita (venditore TECSTORE24)
  - occhioaiprezzi 13/6/2026 ore 15:58: €1.199,00 (1 offerta)
  - Link idealo: https://www.idealo.it/confronta-prezzi/206211153/lg-oled-g5-2025.html
  - Link occhioaiprezzi: https://occhioaiprezzi.com/confronto-prezzi/lg-oled-evo-ai-g5-tv-55-pollici-oled55g55lw-2025/
  - Link MediaWorld: https://www.mediaworld.it/it/product/_lg-oled-evo-g5-oled55g54lw-55-oled-4k-431783.html
- LG OLED G4 55" (OLED55G45LW 2024): non disponibile nuovo; G4S (OLED55G46LS) €1.199 MediaWorld
  - Link idealo G45LW: https://www.idealo.it/confronta-prezzi/204137509/lg-oled-g45lw.html
- LG OLED C5 55" (OLED55C56LB / OLED55C54LA 2025): €999-1.107 idealo
  - occhioaiprezzi 13/6/2026 ore 15:46: €999,00 (1 offerta)
  - Link occhioaiprezzi: https://occhioaiprezzi.com/confronto-prezzi/lg-oled-evo-ai-c5-tv-55-pollici-oled55c56lb-2025/
  - Link idealo: https://www.idealo.it/confronta-prezzi/206250974/lg-oled-c5elb.html
- LG OLED C4 55" (OLED55C44LA 2024): ~€1.099-1.232 idealo — sostituito dal C5 più conveniente
- Sony BRAVIA 8 II 55" (K55XR8M2 / K55XR8M25BP, QD-OLED 2025): €1.438-1.849 idealo/mediaworld
  - MediaWorld: €1.849 spedizione gratuita (sconto da €2.499)
  - Sony Store: €2.049 (prezzo originale €2.099)
  - Link idealo: https://www.idealo.it/confronta-prezzi/206562469/sony-bravia-8-ii.html
  - Link MediaWorld: https://www.mediaworld.it/it/product/_sony-55-bravia-8m2-xr8m2-432348.html
- Sony BRAVIA 9 55": NON ESISTE — la serie 9 parte da 65"
- Sony A95L 55" (XR-55A95L, QD-OLED 2023): €2.599 idealo — ancora in vendita ma vecchio e caro
  - Link idealo: https://www.idealo.it/confronta-prezzi/203246894/sony-xr-55a95l.html
- Philips 55OLED910 55" (OLED+ 2025, B&W audio, Ambilight 4 lati): €2.004-2.123 idealo/pccomponentes
  - Audio: Bowers & Wilkins 3.1 81W con Nautilus tube — miglior audio integrato della categoria
  - Link idealo: https://www.idealo.it/confronta-prezzi/206587625/philips-oled910.html
- Philips OLED909 55" (OLED+ 2024, B&W audio, Ambilight 4 lati): €2.945 idealo — modello 2024, caro
  - Link idealo: https://www.idealo.it/confronta-prezzi/204332551/philips-oled909.html
- Panasonic TX-55MZ2000E (OLED 2023, Soundscape Pro 360°): €2.744 idealo / non disponibile trovaprezzi
  - Modello 2023, fuori produzione — non consigliato a questi prezzi
- Panasonic TX-55MZ1500E: ~€1.647 idealo — ancora disponibile

**Note PREMIUM operative (giugno 2026):**
- Samsung S95F 55" è il BEST VALUE della fascia OLED premium: listino €2.499, acquistabile a ~€1.200
- LG OLED G5 55" sfida il Sony BRAVIA 8 II a prezzo inferiore (~€400 meno) con qualità immagine simile
- LG OLED C5 55" è il MIGLIOR PREZZO per un OLED premium entry con pannello W-OLED di qualità
- Philips 55OLED910 ha il MIGLIOR AUDIO INTEGRATO (B&W 81W Nautilus) ma costa ~€2.100
- Samsung QN90F 55" (Neo QLED) è il MIGLIOR PREZZO per chi vuole Mini LED con anti-riflesso (~€990-1.130)
- Sony BRAVIA 8 II audio: Acoustic Surface Audio+ (vibra il pannello) — tecnologia unica Sony
- Samsung Samsung.com spesso ESAURITO diretto — comprare da rivenditori terzi su MediaWorld/idealo
- occhioaiprezzi.com confermato affidabile per prezzi aggiornati in real-time (verificato 13/6/2026)

**Note operative:**
- Amazon.it e MediaWorld.it sono le fonti principali per TV con spedizione gratuita
- I prezzi TV oscillano molto: offerte flash da -30/-40% frequenti (monitorare hwupgrade.it e tomshw.it)
- amazon.de spesso non spedisce TV in Italia o ha costi di spedizione elevati (>50€ per pannelli grandi)
- Coolblue.nl/de teoricamente spedisce in EU ma non emerge nei risultati: da verificare caso per caso
- Per TV, la garanzia EU è fondamentale: evitare acquisti extra-EU
- Prime Day (luglio) e Black Friday (novembre) sono i momenti migliori per sconti aggiuntivi 20-40%
- Samsung.com/it offre spesso bundle soundbar gratuita su acquisto TV — verificare sempre promozioni attive
- MediaWorld.it (WebFetch): restituisce prezzi strutturati affidabili inclusa spedizione — FONTE AFFIDABILE
- Samsung.com/it (WebFetch): restituisce prezzo, promozioni e bundle attivi — FONTE AFFIDABILE
- Unieuro.it (WebFetch): restituisce solo CSS/HTML senza prezzi — inutile, usare WebSearch snippet
- occhioaiprezzi.com (WebFetch): mostra data esatta ultimo aggiornamento prezzo — UTILE per verificare se prezzo idealo è fresco. Confermato aggiornamento real-time (aggiornato 13/6/2026 ore 10:27 nella sessione corrente)
- idealo.it snippet "oggi" può non essere aggiornato a oggi: verificare sempre su occhioaiprezzi o pagina prodotto retailer
- Quando idealo ha DUE voci per stesso modello (es. "TCL C7K" €539 e "TCL 55C7K" €1003), la voce senza taglia spesso è la 50" o variante diversa — verificare sempre la taglia nel titolo della scheda
- Unieuro fa "Summer Black Friday" periodicamente a giugno — monitorare smartworld.it/volantini per date e offerte TV
