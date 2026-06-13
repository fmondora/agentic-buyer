# SustainabilityScout — Learnings

## Fonti affidabili

### TV / Elettronica di consumo
- **Samsung Sustainability Report PDF** (samsung.com/global/sustainability/media/pdf/) — dati emissioni Scope 1/2/3 precisi, aggiornati annualmente
- **LG Newsroom / lgnewsroom.com** — comunicati ufficiali su certificazioni eco e dati emissioni
- **Sony presscentre** (sony.it/presscentre, sony.eu/presscentre) — informazioni SORPLAS e Road to Zero
- **TP Vision Sustainability Reports** (tpvision.com/sustainability-reports/) — SBTi targets e dettagli packaging; CDP rating disponibile (Climate B, Water A-, Supplier B); EcoVadis Platinum confermato
- **PRNewswire** — comunicati ufficiali Hisense e TCL ESG
- **DitchCarbon.com** — aggregatore dati emissioni aziendali (utile per Samsung, cross-reference); ma spesso restituisce 403 su fetch diretto
- **EthicalConsumer.org** — critica indipendente brand (utile greenwashing check Samsung)
- **TheGoodShoppingGuide.com** — rating etico indipendente (TCL, Philips)
- **TWICE.com** — rivista settore AV, buona copertura certificazioni eco
- **Morningstar/PRNewswire** — comunicati ufficiali su LG eco-certificazioni 2026
- **news.samsung.com/ca** — comunicati TÜV Rheinland certifications dettagliati per modello; anche /sg e /us
- **tcl.com/global/en/news/** — comunicati ufficiali TCL EcoVadis, sustainability journey
- **techbuzz.ai** — analisi indipendente certificazioni Samsung (utile per fact-check che Samsung non pubblica dati CO2e concreti)
- **SammyGuru.com / SamMobile** — copertura certificazioni Samsung modello per modello

### Dati emissioni CO2
- **DitchCarbon.com/organizations/[brand]** — dati Scope 1/2/3 aggregati e confrontabili (attenzione: 403 su fetch diretto, usa risultati via WebSearch)
- **ClimateAction100.org** — valutazione indipendente impegni climatici grandi aziende
- **CDP disclosures** (cdp.net) — rating ufficiali A-D, ma difficile accesso diretto senza account
- **tracenable.com/company/[brand]** — dati climate targets e Scope coverage per azienda

## Fonti problematiche
- **CDP.net** — richiede login per i report dettagliati, dati rating disponibili solo via comunicati terzi
- **EPEAT.net** — database certificazioni verificabile ma query diretta non sempre restituisce risultati consumer TV (meglio per B2B/displays professionali)
- **Siti .cn di Hisense/TCL** — scarsa trasparenza in inglese, dati supply chain non disponibili pubblicamente
- **Trovaprezzi.it** — utile per prezzi, inutile per dati sostenibilità
- **S&P Global ESG Score diretto** — non accessibile senza abbonamento; TCL ha ricevuto 1/100 ma fonte non verificabile online gratuitamente
- **Samsung PDF report diretti** (sustainability/media/pdf/) — spesso immagine compressa, non estraibile via WebFetch
- **news.samsung.com** — spesso timeout su WebFetch; meglio leggere via WebSearch + SammyGuru/SamMobile
- **DitchCarbon.com fetch diretto** — restituisce 403; usare solo via risultati di ricerca

## Pattern di ricerca efficaci

### Per certificazioni prodotto TV
- `"[brand] TV sustainability EPEAT Energy Star EU Ecolabel [anno]"` — funziona per Samsung, LG, Sony
- `"[brand] 55 inch TV recycled materials packaging [anno]"` — buono per materiali specifici
- `"[brand] SORPLAS recycled plastic TV"` — specifico Sony, ottimi risultati
- `"Samsung QLED Neo QLED TÜV carbon reduction certification [anno]"` — ottimo per modelli certificati
- `"[brand] EcoVadis gold rating [anno]"` — per TCL, TP Vision

### Per dati aziendali
- `"[brand] Electronics ESG report [anno] CO2 emissions scope 1 2 3 CDP rating net zero"` — query completa efficiente
- `"[brand] greenwashing controversies environmental violations [anno]"` — per check critico
- `"[brand] sustainability report [anno] biodiversity water"` — specifico impatto ecosistemi
- `"[brand] Emissions Breakdown Climate Score DitchCarbon"` — per trovare aggregate data via search (non fetch)

### Per fascia prezzo/modello specifico
- Combinare ricerca su trovaprezzi.it (prezzi) + scheda prodotto ufficiale brand (specs eco)
- Cercare singolarmente il nome modello + "sustainability" o "recycled" non produce buoni risultati — meglio cercare la policy generale del brand per quella fascia
- Per Samsung certificazioni modello specifico: cercare su news.samsung.com/sg o /ca (meno timeout del /global)

## Note per categoria

### TV 55 pollici fascia fino a 1000€ — OLED (2025-2026)

#### Modelli OLED 55" disponibili entro 1.000€ in Italia (giugno 2026)
- **LG OLED55C5** (2025) — ~826€ su idealo.it — OLED evo, il più accessibile con certificazioni eco complete
- **LG OLED55B5** (2025) — sotto 900€ — OLED entry, meno certificazioni del C5 ma stessa tecnologia di pannello
- **Samsung S85H 55"** (2026) — prezzo da verificare — OLED Samsung con TÜV Rheinland Carbon Reduction
- **Sony Bravia 8 / A80L 55"** — min ~1.299€ — FUORI BUDGET a 1.000€, tutte le Sony OLED 55" sono sopra 1.000€

#### Sostenibilità OLED vs LCD
- OLED LG: stima riduzione 80.000 ton CO2 nel 2026 vs LCD equivalente (dato ufficiale LG, non verificato indipendentemente)
- OLED ha efficienza energetica superiore in uso reale (pixel off = zero consumo per nero)
- LG C6 55" (2026): E-Cycle Excellent Products (Korea, 4° anno consecutivo); Carbon Trust Reducing CO2 per modelli ≥65"; Intertek Resource Efficiency (8 serie)
- LG C6 83"/77": EU Energy Label D (miglioramento rispetto a E/F di alcuni LCD)
- Samsung S85H (2026): TÜV Rheinland Product Carbon Reduction certification; Product Carbon Footprint per 48"

### TV 55 pollici fascia fino a 1000€ — QLED (2025-2026)

#### Modelli QLED 55" disponibili entro 1.000€ in Italia (giugno 2026)
- **Samsung QLED Q60/Q65 55"** (2026) — ~500-700€ — entry QLED Samsung
- **Samsung Neo QLED QN85F/QN90F 55"** (2026) — ~900-950€ — Mini LED, TÜV certified
- **TCL C7L/C7K 55"** (2026) — ~700-900€ — QD-Mini LED
- **TCL C8L 55"** (2025/2026) — ~805€ — QLED premium
- **Hisense U6/U7 ULED 55"** (2026) — ~350-700€ — Mini LED QLED
- **Philips PQS9001 55"** (2026, da giugno) — prezzo da confermare, stima 600-800€ — QLED "The One"

#### Certificazioni QLED specifiche (importante distinguere da OLED)
- **Samsung**: le certificazioni TÜV Carbon Reduction 2026 coprono principalmente OLED (S90H, S85H) e Micro RGB — i modelli QLED base (Q60, Q65) NON sono inclusi nelle 14 certificazioni Carbon Reduction. I Neo QLED (QN85F, QN90F) hanno ricevuto Product Carbon Footprint (non Reduction) in anni precedenti (5° anno consecutivo).
- **Dato CO2e riferimento**: QLED 75Q60C = 982 kg CO2e ciclo vita (dato 2023, unico valore trovato pubblicamente per QLED base)
- Samsung pubblica % materiali riciclati (31% su plastica nel 2024) ma NON pubblica kg CO2e specifici per modello 2026 nei comunicati certificazioni
- **TCL**: certificazioni ISO 14067 su 33 prodotti (2025 ESG report) — non specificato se include TV QLED; EcoVadis Gold 80/100 (2025); nessuna Energy Star o EU Ecolabel confermata su TV QLED
- **Hisense**: nessuna certificazione prodotto specifica (EPEAT, Energy Star, EU Ecolabel) trovata per QLED U6/U7; certificazioni ISO 14001 su 41 stabilimenti (processo, non prodotto)
- **TP Vision/Philips**: CDP B clima, A- acqua; EcoVadis Platinum; SBTi -42% Scope 1/2/3 use-phase entro 2030 — dati prodotto specifici non trovati per PQS9001

#### Emissioni CO2 aziendali brand QLED (dati 2024-2025)
- **Samsung**: Scope 1 ~3,7 Mt CO2e, Scope 2 ~9,6 Mt CO2e, Scope 3 ~125 Mt CO2e totale (2024); CDP A (Leadership 2025); MSCI AA (2025); net-zero 2050 (DX 2030 per S1+S2)
- **TCL Industries**: Scope 1 ~289 kt CO2e, Scope 2 ~177 kt CO2e (2024, -43% vs 2023); Scope 3 NON DICHIARATO; nessun CDP rating trovato
- **Hisense Home Appliances**: Scope 1 ~40 kt CO2e, Scope 2 ~341 kt CO2e (2022, ultimi dati pubblici); Scope 3 NON DICHIARATO; carbon peaking by 2026, neutrality by 2050
- **TP Vision**: CDP B clima, A- acqua; dati Scope assoluti non trovati online; SBTi approvato 2022

#### Packaging QLED
- Samsung: EPS riciclato 10% + accessori con plastica riciclata 50%, cartone FSC
- TCL: soia ink + FSC + cartone riciclabile; primo honeycomb packaging (no polistirolo); ABS riciclabile
- Hisense: non trovato dettaglio specifico QLED
- TP Vision/Philips: transizione verso packaging plastica-free, cartone riciclato

#### Note biodiversità brand QLED
- Samsung DS Division: causa legale (marzo 2025) contro governo coreano per approvazione complesso Yongin (10GW consumo) — contesto semiconductor, non TV
- TCL: nessuna controversia specifica trovata; claim "green manufacturing" verificabili via ISO 14001 su 34 sussidiarie
- Hisense: WEF Lighthouse Factory (Huangdao, VRF) — positivo; nessuna controversia ambientale specifica trovata
- TP Vision: piccola azienda, nessuna controversia rilevata

### TV 55 pollici fascia 400-600€ (2025-2026) — generale
- In questa fascia i modelli di punta eco sono: LG UR78/UR81 (LED 4K), Samsung U8000F/Crystal UHD, Sony KD-X75/X85 series, Hisense U6/E6, TCL C6/Q651G, Philips PUS8xxx
- I TV OLED (più sostenibili per tecnologia) sono quasi tutti sopra i 600€ a 55"
- La maggior parte delle certificazioni eco (EPEAT Gold, Carbon Trust) si trovano sui modelli OLED premium — le linee entry/mid come Crystal UHD o UR78 hanno meno certificazioni specifiche per modello, ma ereditano la policy aziendale
- **LG** e **Sony** sono i brand più trasparenti su materiali riciclati specifici per modello
- **Samsung** ha ottima trasparenza aziendale (Scope 1/2/3 pubblici, MSCI AA) ma controversie semiconductor DS Division
- **TCL** ha S&P ESG score molto basso (1/100 segnalato) — scarsa trasparenza supply chain; ma EcoVadis Gold 80/100 (2025) è dato più recente e verificabile
- **Hisense** fa claim ESG aggressivi ma scarsa trasparenza su emissioni Scope 3 e supply chain dettagliata
- **TP Vision/Philips** (TV) è separato da Philips Medical — SBTi approvati, ma azienda medio-piccola con meno risorse ESG
- Il carbon footprint di un TV 55" LCD tipico: ~1.200 kg CO2e per unità (dato ISO 14067 su TCL 55P8K)
- QLED 75Q60C Samsung: 982 kg CO2e ciclo vita (dato 2023) — leggermente migliore per efficienza energetica
- LG OLED stima risparmio 80.000 ton CO2 totale 2026 vs LCD equivalente
- Packaging: Samsung usa EPS riciclato 10% + cartone FSC; LG usa cartone monocromatico riciclabile; TCL usa soia ink + FSC; Sony in transizione verso plastica-free
- Energy Star certificazione: Samsung e LG coprono linee principali; TCL ha copertura parziale; Sony ha Energy Star su modelli principali USA
- EPEAT: principalmente per display professionali — raro su consumer TV economici

### Sony OLED — nota budget
- Sony A80L 55" minimo ~1.299€, Sony Bravia 8 55" ~1.499€: entrambe FUORI dal budget 1.000€
- Le certificazioni Sony (CDP A-List, SBTi, SORPLAS 60% plastica riciclata) si applicano anche agli OLED, ma il prodotto non è acquistabile entro budget
- SORPLAS su OLED: rear cover in plastica riciclata, riduzione CO2 57% vs plastica vergine equivalente
- Dal 2025 Sony ha chiuso il loop: le rear cover dei TV dismessi vengono riciclate in nuovo SORPLAS

### Greenwashing alert per categoria TV
- **Samsung QLED base (Q60/Q65)**: certificazioni TÜV 2026 non coprono questi modelli — solo OLED e Micro RGB hanno Carbon Reduction. I Q60/Q65 hanno meno trasparenza ambientale a livello di prodotto specifico. Rilevante: scoperto nel 2022 che i Neo QLED riconoscevano i test benchmark (rimosso dopo controversia). Segnala disallineamento marketing/realtà.
- **Hisense**: claim "green revolution" e "lighthouse factory" ben documentati WEF, ma nessun Scope 3 supply chain pubblicato dettagliatamente — prudenza; carbon peaking 2026 non ancora verificabile
- **TCL**: S&P ESG 1/100 è un segnale datato; EcoVadis Gold 80/100 (2025) più recente e credibile; ISO 14067 su 33 prodotti positivo; Scope 3 mai dichiarato è il gap principale
- **Samsung DS Division** (semiconductors): controversia concreta su nuovo complesso Yongin (10GW consumo, 3GW da LNG) — non impatta direttamente TV DX Division ma segnala disallineamento interno
- **Sony** è il più credibile in assoluto (CDP A-List, SBTi approvato, MSCI AAA 6 anni consecutivi, SORPLAS verificabile) ma i QLED non sono nel portfolio Sony — Sony fa solo LCD entry e OLED premium
- **TP Vision/Philips**: EcoVadis Platinum, CDP B/A-, SBTi — credibile; meno visibilità su prodotto specifico QLED
