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

### Tavole/pannelli larice per rivestimento parete interno (analisi giugno 2026)

**Indice riparabilità francese/iFixit:** Non applicabile a materiali da costruzione/rivestimenti. Categorie non coperte da nessuno dei due sistemi.

**Classe di durabilità naturale larice (UNI EN 350):** Classe 3-4 (moderatamente durabile). In uso interno asciutto (umidità < 20%) la durabilità è di fatto illimitata — il fattore limitante non è la resistenza del materiale ma la manutenzione estetica. La durata di 4-7 anni dichiarata da alcune fonti si riferisce a condizioni sfavorevoli (esterno esposto). In interno ben condizionato: stima realistica 50-100+ anni.

**Trattamento post-posa:**
- Lasciare naturale: possibile e accettabile esteticamente. Il larice ingiallisce/scurisce progressivamente per ossidazione e UV (anche da finestre), assumendo una patina ambrata poi brunita. Non è un danno ma una trasformazione estetica.
- Olio (es. Rubio Monocoat Oil Plus 2C, Osmo Polyx): protezione idrorepellente + controllo colore. Nessun film, penetra nel legno. Manutenzione: ritrattamento ogni 5-10 anni per pareti (molto meno usura che pavimenti), o quando il colore sbiadisce visibilmente.
- Impregnante: protezione maggiore, più film in superficie. Ritrattamento ogni 5-6 anni con carteggiatura leggera.
- Vernice: film duro, protegge molto ma si screpola nel tempo, richiede carteggiatura completa a ogni ritrattamento.
- Cera: per uso interno ornamentale, ritrattamento ogni 2-3 anni — meno usato su pareti.
- Consiglio pratico: olio monocomponente (es. Osmo, Rubio) è il migliore equilibrio per pareti rustiche: protegge, valorizza la venatura, ritrattamento facile senza carteggiatura.

**Evoluzione cromatica in interno:**
- Anno 0: giallo dorato / rosso-brunastro con nodi evidenti
- Anno 1-3: ossidazione progressiva, il colore si scalda verso ambra/miele
- Anno 5-10: patina bruna calda, nodi più scuri, aspetto "vissuto"
- Senza UV diretti e senza trattamento: processo molto lento (decenni)
- Con esposizione solare diretta da finestra: processo accelerato in 2-5 anni
- Con olio: colore stabilizzato, processo rallentato significativamente

**Criticità specifiche del larice rustico:**
- **Resina**: il larice può essudare resina (specialmente nei nodi) per i primi 1-3 anni, soprattutto con riscaldamento. Normale, si tampona con solvente (trementina o alcool). Non è un difetto strutturale.
- **Ritiro**: tavole non stagionate adeguatamente possono retrarre con il riscaldamento invernale (fessure tra tavole). Prevenire con stagionatura pre-posa (7-10 giorni in ambiente dove verrà montato) e gap di 2-3mm tra tavole.
- **Nodi cadenti** (grado rustico): in qualità rustica i nodi non aderenti possono cadere. Trattamento: stucco al quarzo compatibile con il legno o resina epossidica trasparente.

**Riparabilità (sostituzione singolo pannello):**
- Profili con incastro maschio-femmina (perline): sostituzione singola difficile senza smontare dall'alto verso il basso. Possibile ma laborioso.
- Profili a clips/vite a vista: sostituzione singola facile, fai-da-te accessibile.
- Tavole con vite a vista: sostituzione triviale, bullone/vite accessibile.
- Criticità cromatica: una tavola nuova sarà visibilmente più chiara di quelle invecchiate. Soluzioni: imbrunimento artificiale (acido tannico + solfato ferroso, o impregnante colorato scuro), oppure sostituire una zona intera per uniformità.
- Ricambi: il larice è essenza comune, disponibile nei legnami locali senza problemi. Costo ~30-70 €/m2 per tavole nuove.

**Fine vita:**
- Il legno massiccio è il materiale da costruzione con il ciclo di vita più virtuoso.
- Riuso diretto: tavole in buono stato vengono ricomprate da operatori specializzati in legno di recupero (es. Wood Revive, Torreano, Volgger Holz). Il larice antico ha valore di mercato superiore al larice nuovo per l'aspetto vissuto.
- Riciclo: in caso di impossibilità al riuso, il legno si ricicla in pannelli MDF/truciolare o viene usato come combustibile (pellet/cippato).
- Compostaggio: possibile se non trattato con vernici/impregnanti biocidi.
- RAEE: non applicabile — il legno non è RAEE. Va conferito come rifiuto verde o ingombrante, oppure portato al centro di raccolta (isola ecologica) — filiera rifiuti speciali se trattato con biocidi.

**Prezzi pannelli larice (giugno 2026):**
- Larice grezzo/rustico: ~€30-70/m2 per tavole lavorate
- Larice per rivestimento esterno: ~€50-100/m2
- Larice antico di recupero (rivestimento): ~€60-120/m2 (premium per effetto vissuto immediato)
- Nella fascia richiesta (fino a €60/pannello per 80x200x1,8cm = 1,6m2): ~€37,5/m2 — fascia bassa-media, compatibile con larice rustico di qualità A/B o speziato

**Fonti affidabili per legno/materiali costruzione:**
- pgcasa.it — caratteristiche, prezzi, durata larice (affidabile)
- pandawood.it — schede tecniche essenze legnose, comportamento in interno
- woodrevive.it — legno di recupero, valore riuso larice antico
- rubiomonocoat.it — trattamento olio legno interni, manutenzione
- garbelotto.it — specie legnose, caratteristiche tecniche
- infobuild.it — normative edilizia, classi durabilità, UNI EN 350
- zennarolegnami.com — profili larice, qualità, dimensioni disponibili
- risponde.promolegno.com — Q&A tecnico su legno (Promo_Legno, associazione di settore)

**Fonti problematiche per questa categoria:**
- assolegnorisponde.it — certificato SSL non valido, WebFetch fallisce
- ottolinilegnami.com/post — pagina 404
- adler-italia.it — pagina JS-heavy, solo CSS nel contenuto

### Fitness tracker / Smart band fascia 100-200€ — analisi approfondita giugno 2026 (aggiornamento)

**WHOOP 5.0 — modello subscription device-as-a-service:**
- Il device NON è di proprietà dell'utente nel modello USA standard: si "affitta" con la membership
- In Italia (test da maggio 2026): WHOOP sta sperimentando vendita separata device (69€) + subscription 199€/anno
- Aggiornamento hardware: chi ha 12+ mesi di membership rimanente riceve il nuovo hardware gratis al lancio
- Quando si cancella la membership: il device deve essere restituito (restocking fee $110 se non restituito in USA)
- Upcycle: WHOOP incoraggia a regalare il vecchio device a un amico (programma ricompensa $50 credito accessori)
- Nessun trade-in formale: no programma ritiro/riciclo ufficiale — solo suggerimento di riciclare responsabilmente
- IP68 + silicone, testato per CrossFit intenso (review the5krunner confermata per uso professionale)
- Strap sostituzione: cinturini sostitutivi di terze parti disponibili su Amazon (silicone waterproof)
- Mercato usato WHOOP: quasi inesistente in Italia (il device senza membership attiva è inutilizzabile, o richiede nuova sub)

**Google Fitbit Air — nuova piattaforma Google Health (maggio 2026):**
- Fitbit app → Google Health: migrazione automatica completata maggio 2026, dati storici migrati su Google Account
- Legacy Fitbit Web API: shutdown settembre 2026 (API di terze parti, non il device)
- Il device Fitbit Air è NUOVO (lancio 2025): supporto dichiarato almeno fino a febbraio 2028 (politica Google: 2 anni dopo fine vendita)
- Garanzia EU: 2 anni (EEA) — Google sostituisce con unità ricondizionata se difetto di fabbrica
- Pixel Care+: protezione aggiuntiva acquistabile entro 30 giorni dall'acquisto (copre riparazioni/sostituzioni)
- Housing: policarbonato riciclato + PBT — cinturino tessile con fibbia in acciaio inox
- Cinturino: sistema quick-swap, ricambi first-party (silicone Active Band, nylon Performance Loop) + third-party
- iFixit: nessun teardown o score per Fitbit Air (dispositivo troppo recente/sigillato)
- Valore usato: mercato limitato, Fitbit Air su BackMarket UK ~£80 (stimato 60-80€ in Italia)

**Amazfit Helio Strap — screenless tracker con Zepp App:**
- Nessun abbonamento richiesto (differenziatore chiave vs WHOOP)
- Update policy: Zepp Health ha esteso a 3+ anni per modelli strategici; Helio Strap incluso esplicitamente (aggiornamenti Sept 2025, Dec 2025 confermati, rollout anche in Italia)
- Garanzia: 12 mesi ufficiale Amazfit, ma 2 anni per legge EU nei negozi europei
- Cinturino: sistema standard 22mm quick-release; ampia disponibilità third-party (silicone, nylon) da ~7-15€ su Amazon
- Waterproof: non specificato IP68, verifica in corso — adeguato per sudorazione ma verificare per nuoto
- iFixit: nessun teardown (prodotto di nicchia, non coperto)
- Indice riparabilità FR: non applicabile (smart band non coperta)
- Valore usato: molto basso per prodotti screenless di nicchia (stimato 20-40€ dopo 2-3 anni)

**Garmin Vivosmart 6 — prodotto NON ancora disponibile (giugno 2026):**
- Lancio previsto: annuncio probabile maggio-giugno 2026 (the5krunner), disponibilità effettiva da determinare
- Prezzo atteso: €150-180 (stima da leak)
- Nessun dato ufficiale su specifiche, waterproofing, strap, supporto software
- Per il ciclo di vita: dati proxy da Vivosmart 5 (Garmin track record eccellente, strap quick-release, supporto pluriennale)
- Garmin storico: mai dichiarato EOL anticipato su fitness tracker, aggiornamenti attivi >3 anni su tutti i modelli
- iFixit Garmin (proxy Venu Sq): score 3/10 — involucro difficile da riaprire; strap rimane l'unico componente user-serviceable
- ATTENZIONE: valutazione incerta per definizione — prodotto non sul mercato al momento dell'analisi

**Fonti aggiuntive affidabili per questa categoria:**
- tuttotech.net — notizie WHOOP italia, vendita separata device confermata maggio 2026
- the5krunner.com/2025/10/31/... — review approfondita WHOOP 5.0 per atleti CrossFit
- pasqualepillitteri.it/en/news/... — analisi Fitbit Air e transizione Google Health 2026
- support.whoop.com/s/article/Upcycling — procedura upcycling WHOOP (gifting + credito accessori)
- support.google.com/product-documentation — garanzia Fitbit Air EU 2 anni confermata
- technowize.com/vivosmart-6-leak — specifiche leaked Vivosmart 6

**Fonti problematiche:**
- eBay.it per WHOOP usato: praticamente nessun annuncio (il device senza abbonamento è inutile)
- Subito.it WHOOP: solo accessori (caricatori), non device completo

### Fitness band cinesi fascia 35-250€ — analisi ciclo di vita (giugno 2026)

**Huawei Band 9 e Band 11 Pro — limitazione acqua calda CRITICA:**
- Entrambi i device Huawei dichiarano esplicitamente di NON indossare in acqua calda, docce calde, saune
- consumer.huawei.com/it (pagina specs Band 11 Pro) conferma: "not intended to be worn during hot showers, hot spring immersion, or saunas"
- Per CrossFit (doccia post-allenamento), questa è una limitazione operativa reale che riduce la vita del sigillo
- Politica software Huawei per wearable: 24 mesi dichiarati — corta rispetto ai competitor
- Connettore proprietario che cambia generazione (Band 9 ≠ Band 11 Pro) — ecosistema strap non retrocompatibile
- Assistenza Huawei Italia strutturata: consumer.huawei.com/it con riparazione postale gratuita
- Score ciclo di vita: Band 11 Pro 5/10, Band 9 4/10

**Xiaomi Smart Band 10 Pro — miglior ciclo di vita della categoria cinese:**
- Lancio globale 28 maggio 2026 — prodotto recentissimo
- HyperOS 3 già rilasciato su Band 10 standard (dicembre 2025); Band 10 Pro attesa HyperOS 3+ nei prossimi mesi
- Connettore compatibile con Band 8/9/10 (3 generazioni stabili) — ecosistema ricambi ampio
- Cinturini ufficiali su mi.com/it + terze parti abbondanti (Niboow compatibile Band 10/9/8 su Amazon.it)
- Nessuna limitazione acqua calda dichiarata (5ATM + IP68)
- Score ciclo di vita: 6/10

**Honor Band 9:**
- Politica 7 anni aggiornamenti Honor si applica SOLO alla serie Magic smartphone — NON alle smart band
- Per Band series Honor: politica effettiva 2-3 anni firmware (simile a Huawei)
- Nessuna limitazione acqua calda dichiarata
- Rete assistenza Honor in Italia meno capillare di Huawei
- Score ciclo di vita: 4.5/10

**JCVital Pro V8 ECG e Hume Band 2.0 — brand senza ecosistema EU:**
- JCVital = brand di Shenzhen Youhong Technology Co. / Jointcorp (produttore OEM/ODM) — senza distribuzione EU strutturata
- Hume Band = startup USA direct-to-consumer, forte dipendenza da server cloud — se l'azienda chiude il device diventa inutile
- Entrambi venduti in USD da siti USA: la garanzia EU minima di 2 anni NON si applica automaticamente agli acquisti fuori UE
- Garanzia Hume: 1 anno standard + opzione "a vita" per $35 (HumeCare) — trovata marketing senza track record
- Nessun centro assistenza autorizzato in Italia/EU per entrambi i brand
- Zero ricambi disponibili su Amazon.it/EU
- Zero mercato usato identificabile in Italia (eBay, Subito)
- Score ciclo di vita: JCVital 2/10, Hume 2/10
- Hume Health Trustpilot (humehealth.com, giugno 2026): 3.6/5 su 4.152 recensioni — problemi principali: rimborsi non processati (attesa mesi), prodotti non consegnati, customer service >5gg risposta, inaccuratezze sensori. Il dato "1.4/5" citato in alcuni brief e probabilmente riferito a una pagina specifica o periodo precedente.
- JCVital = brand front su sito Shopify (jcvital.com) senza termini di garanzia pubblicati pubblicamente. Garanzia verificabile solo contattando direttamente il produttore.

**Benchmark ciclo di vita per fitness tracker (riferimento per confronti):**
| Brand/Device | Score ciclo di vita | Note chiave |
|---|---|---|
| Garmin Vivosmart 5/6 | 8/10 | Assistenza EU, 3+ anni SW, sostituzione device ufficiale ~50-80€, cinturino quick-release |
| WHOOP 5.0 | 7/10 (con sub) | Hardware sostituito gratis ogni generazione per abbonati, ma device inutile senza abbonamento |
| Fitbit Air (Google) | 6.5/10 | Garanzia EU 2 anni, cinturino quick-swap, 2 anni SW garantiti, valore usato ~60% |
| Xiaomi Band 10 Pro | 6/10 | Miglior cinese — connettore 3 generazioni stabile, ampi accessori, IP68 |
| Huawei Band 11 Pro | 5/10 | Assistenza IT strutturata ma limitazione acqua calda = problema CrossFit |
| Honor Band 9 | 4.5/10 | No limitazione acqua calda ma assistenza IT meno capillare |
| Huawei Band 9 | 4/10 | Limitazione acqua calda, supporto 24 mesi, usa-e-getta |
| JCVital Pro V8 / Hume Band 2.0 | 2/10 | Brand senza distribuzione EU, server cloud come punto di failure, zero assistenza IT |

**Regola generale per brand DTC americani/cinesi senza distribuzione EU:**
- La garanzia commerciale del venditore (1 anno) è l'unica protezione — la garanzia EU non si applica
- Dipendenza da app/server cloud = rischio di inutilizzabilità se il brand viene acquisito, pivot, o chiude
- Zero valore usato su mercati italiani (nessun acquirente conosce il brand)
- Contromisura: usare PayPal o carta di credito con protezione acquisti come assicurazione aggiuntiva

**Batteria come limite reale per uso CrossFit:**
- Nessun device di questa fascia ha batteria user-replaceable
- Uso CrossFit intenso (GPS + HR continuo) degrada la batteria più rapidamente della media
- Stima vita utile realistica: 18-30 mesi prima che l'autonomia diventi inaccettabile per tutti questi modelli

**Cinturini per CrossFit:**
- Xiaomi Band 10 Pro: meglio equipaggiata (opzioni silicone, nylon traspirante, ceramica)
- Huawei Band 11 Pro: fluoroelastomero ufficiale (resistente a sudore) + nylon
- Huawei Band 9: rapida sostituzione, 49 offerte su trovaprezzi da ~7,80€
- Honor Band 9: cinturini su Amazon — compatibilità con sistema semi-proprietario

**Fonti affidabili per questa categoria:**
- consumer.huawei.com/it/wearables/band11-pro/specs/ — specs e limitazioni acqua calda
- mi.com/it/product/xiaomi-smart-band-10-pro/ — specs ufficiali Band 10 Pro
- gizchina.it — accessori Xiaomi Band 10 Italia
- notebookcheck.net — notizie lancio Band 11 Pro Europa
- smartwatchinsight.com — leak Xiaomi Band 10 Pro
- versus.com — confronti spec tra band
- consumer.huawei.com/ie/support/warranty-policy/ — garanzia Huawei wearable 24 mesi confermata (pagina IE, stessa policy EU)
- wareable.com/health-tech/hume-band-2-0-review — review Hume Band 2.0 indipendente 2026
- healnourishgrow.com/hume-band-review/ — analisi Hume Band 2.0 con confronto vs WHOOP
- jointcorp.com — sito produttore Jointcorp (JCVital), profilo OEM/ODM Shenzhen Youhong Technology

**Fonti problematiche per questa categoria:**
- JCVital su eBay: zero risultati usato — brand non presente nel mercato secondario italiano
- Hume Band su Subito.it/eBay.it: zero annunci — mercato secondario inesistente in Italia
- consumer.huawei.com/it/support/warranty-policy/wearables/ — WebFetch restituisce contenuto ma non i dettagli specifici per Band series; dati garanzia 24 mesi verificati tramite altri canali
- trustpilot.com (WebFetch diretto) — restituisce 403; usare WebSearch per leggere snippet e rating
- jcvital.com warranty/refund page — non indicizzata su Google; la policy non e pubblica, accessibile solo navigando il sito direttamente

### Fitness tracker / Smart band fascia fino a 200€ (analisi giugno 2026)

**Indice riparabilità francese:** NON applicabile alla categoria fitness tracker/smart band. Il regolamento francese copre: smartphone, laptop, aspirapolveri, lavastoviglie, idropulitrici, lavatrici. I wearables/smart band non rientrano nelle categorie con obbligo di indice.

**iFixit — copertura fitness tracker:**
- **Fitbit Charge 6**: score 4/10 — unico fitness tracker nella categoria con score ufficiale iFixit. Design sigillato, priorità waterproofing su riparabilità. Solo il cinturino è user-serviceable.
- **Garmin Venu Sq Music Edition**: score 3/10 — proxy per la filosofia costruttiva Garmin su fitness tracker. Pessimo come smartwatch Garmin.
- **Amazfit, Xiaomi, Samsung Fit 3, Huawei Band**: nessun score iFixit disponibile per le smart band di fascia bassa. iFixit non copre questi prodotti.
- **Garmin Vivosmart (prima generazione)**: teardown disponibile ma senza score numerico; involucro con silicone sealant intorno, difficile da riaprire.

**Batteria nelle smart band — problema strutturale:**
- In TUTTE le smart band di questa fascia la batteria è sigillata e non user-replaceable.
- Sostituzione ufficiale: possibile solo tramite service center del brand a costo variabile (spesso non conveniente rispetto al prezzo del device).
- Garmin: servizio ufficiale invia unità ricondizionata (non ripara la batteria), costo ~50-80€, può richiedere 2-4 settimane.
- Xiaomi, Amazfit, Huawei: assistenza tramite centri autorizzati; per prodotti con prezzo <100€ spesso non economicamente conveniente riparare.
- Samsung Galaxy Fit 3: assistenza Samsung, stesso approccio — device sotto i 50€ praticamente mai conveniente riparare.
- **Conseguenza**: quando la batteria degrada (tipicamente 2-3 anni di uso intenso) il device diventa rifiuto elettronico, tranne se si riesce a trovare un centro specializzato in riparazione wearables.

**Supporto software — rischi critici per categoria:**

| Brand/Device | Supporto software | Rischio |
|---|---|---|
| Fitbit Charge 6 | Fine supporto firmware Q3 2026; brand in dismissione da Google entro fine 2026 | **CRITICO — supporto già terminato** |
| Garmin Vivosmart 5 | Aggiornamenti confermati fino a marzo 2026+, nessuna data EOL dichiarata; storico Garmin eccellente | Basso |
| Amazfit Band 7/8/9 | Policy estesa a 3+ anni per modelli strategici; Band serie non inclusa esplicitamente nell'estensione | Medio |
| Xiaomi Smart Band 9 Pro | HyperOS 2 (nov 2024), HyperOS 3 confermato (dic 2025); aggiornamenti attivi | Basso-medio |
| Samsung Galaxy Fit 3 | 2-3 anni garantiti (lancio 2024 → supporto fino ~2027); aggiornamenti confermati a feb 2026 | Basso |
| Huawei Band 9 | HarmonyOS 4.2 ricevuto; politica ufficiale: 24 mesi di aggiornamenti | Medio |

**Waterproofing per uso intenso CrossFit/doccia:**
- IP68 + 5ATM = protezione fino a 50m × 10 minuti (standard). Adeguato per nuoto, doccia, sudorazione.
- Huawei Band 9: **ufficialmente sconsigliato in doccia calda** (il costruttore stesso lo indica — acqua calda + detergente degradano il sigillo). Critico per uso CrossFit+doccia frequente.
- Galaxy Fit 3: confermato affidabile in doccia e nuoto da test reali 6 mesi (aliexpress wiki + androidauthority).
- Garmin Vivosmart 5, Xiaomi Band 9 Pro, Amazfit Band 9: 5ATM + IP68 dichiarati. Garmin ha track record eccellente su waterproofing di serie.
- **Cinturini**: per uso CrossFit preferire cinturini in silicone morbido (sweat-resistant, asciuga veloce) o nylon (Xiaomi ha opzione ufficiale nylon).

**Cinturini sostitutivi — ecosistema accessori:**
- Xiaomi Band 9 Pro: connettore standard con meccanismo quick-release; ampia disponibilità cinturini ufficiali e third-party (silicone, nylon, metallo) da ~7€
- Garmin Vivosmart 5: cinturini Garmin originali + terze parti disponibili (StrapsCo, Amazon); sistema quick-release
- Huawei Band 9: quick-release; ricambi su Amazon.it da ~8€, trovaprezzi ha 49 offerte da 7,80€
- Fitbit Charge 6: cinturini disponibili su cinturinowatch.it e trovaprezzi; sistema proprietario Fitbit ma ampia compatibilità terze parti da ~15€
- Samsung Galaxy Fit 3: cinturini su Amazon IT, eBay, sistema standard 20mm

**Valore usato stimato (2-3 anni — smart band fascia economica):**
- Smart band economiche (<60€ nuove) hanno valore residuo quasi nullo dopo 2-3 anni: 5-20€ massimo
- Smart band fascia media (60-200€ nuove):
  - Fitbit Charge 6 (nuovo ~110€) → valore usato 2026: 40-70€ (BackMarket ~£108 UK, refurbed.it 127€ ricondizionato)
  - Garmin Vivosmart 5 (nuovo ~130€) → valore usato 2025: 60-90€
  - Xiaomi Smart Band 9 Pro (nuovo ~48€) → valore residuo quasi nullo: 10-20€
  - Samsung Galaxy Fit 3 (nuovo ~32€) → praticamente nessun mercato usato: 5-15€
  - Amazfit Band 9 (~40-50€ nuovo) → mercato usato limitato: 10-20€
  - Huawei Band 9 (~25€ nuovo) → valore residuo trascurabile: 5-10€
- Brand con mercato usato riconoscibile: Fitbit e Garmin

**Trade-in:**
- Garmin: nessun programma trade-in diretto
- Xiaomi: partnership Recommerce per trade-in in 13 paesi EU inclusa Italia (lanciato settembre 2025) — ma probabilmente non copre smart band, solo smartphone
- Amazfit: programma trade-in esistito nel 2022 ma solo USA; non confermato per EU 2025-2026
- Samsung, Fitbit, Huawei: nessun programma trade-in per fitness tracker in Italia

**RAEE smart band:**
- Tutte le smart band contengono batteria Li-Po non rimovibile → conferire obbligatoriamente in isola ecologica come RAEE (categoria "piccoli apparecchi elettronici") — NON in pattumiera
- In alternativa: punti ritiro RAEE in negozi elettronica (Unieuro, MediaWorld, MediaMarkt)

**Prezzi accertati Italia giugno 2026:**
| Modello | Prezzo nuovo | Fonte |
|---|---|---|
| Fitbit Charge 6 | ~110-121€ | idealo.it |
| Garmin Vivosmart 5 | ~130-134€ | idealo.it |
| Xiaomi Smart Band 9 Pro | ~48-50€ | idealo.it / Amazon.it |
| Samsung Galaxy Fit 3 | ~32-35€ | idealo.it |
| Huawei Band 9 | ~25-30€ | trovaprezzi.it |
| Amazfit Band 9 | ~40-50€ (stimato) | trovaprezzi.it (non trovato esatto) |

**Fonti affidabili per fitness tracker/smart band:**
- oxygenfit.co.uk — analisi approfondita Fitbit EOL, dati support timeline confermati
- the5krunner.com — Amazfit support policy changes febbraio 2026
- xiaomitime.com — aggiornamenti HyperOS Xiaomi Band 9 Pro
- sammobile.com / sammyfans.com — aggiornamenti Samsung Galaxy Fit 3
- androidauthority.com — review Samsung Galaxy Fit 3 con test durabilità reale
- huaweicentral.com — aggiornamenti HarmonyOS Huawei Band 9
- consumer.huawei.com/it — avvisi ufficiali waterproofing Huawei (doccia calda sconsigliata)
- ifixit.com/repairability/smartwatch-repairability-scores — unico score iFixit per wearables (Fitbit Charge 6: 4/10)

**Fonti problematiche per questa categoria:**
- idealo.it "Amazfit Band 9" — non restituisce pagina diretta del prodotto nella ricerca Google; preferire trovaprezzi.it per Amazfit
- Ricerche "Amazfit Band 9 CrossFit review" — confondono con Xiaomi Band 9; i due prodotti sono diversi

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
