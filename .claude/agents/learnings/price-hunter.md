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
