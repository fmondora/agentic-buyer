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
- **news.panasonic.com/global** — comunicati CDP, SBTi, MSCI, GREEN IMPACT; dati Scope 1/2/3 disponibili via newsroom (403 su fetch diretto delle pagine dati)
- **lgnewsroom.com / lg.com/global/newsroom** — eco-certifications annuali OLED (Carbon Trust, Intertek, E-Cycle) — fonte primaria per LG
- **ditchcarbon.com/organizations/panasonic** — aggregatore dati Panasonic CO2 (Scope 1+2+3 FY2024 presenti)
- **esgnews.com / esgtoday.com** — aggiornamenti SBTi approvazioni (utile per Sony, Panasonic)
- **theclimatepledge.com** — storie brand Amazon Climate Pledge (Sony documentato bene)

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

### Per fascia premium (OLED, QD-OLED, 1.500-5.000€)
- `"[brand] OLED 55 sustainability recycled materials certification [anno]"` — funziona per Sony, LG, Panasonic
- `"[brand] CDP A-List [anno] climate water"` — efficiente per confermare CDP rating aggiornato
- `"[brand] MSCI ESG rating [anno]"` — buon proxy rapido di reputazione ESG aggregata
- `"Panasonic GREEN IMPACT sustainability TV consumer electronics [anno]"` — per trovare dati TV specifici Panasonic
- `"Loewe TV sustainability Germany recycled"` — dare peso a fonte loewe-outlet.tv (blog ufficiale) e trustedreviews per Syno-Stone
- `"Sony BRAVIA SORPLAS recycled plastic rear cover [anno]"` — ottimo per trovare dati specifici SORPLAS
- `"LG OLED Carbon Trust Reducing CO2 [anno]"` — molto specifico, sempre citato nei comunicati LG OLED

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

### TV 55 pollici fascia premium fino a 5.000€ (2025-2026)

#### Emissioni CO2 aziendali brand premium

- **Samsung** (QD-OLED S95F/S95G): dati identici alla sezione QLED — Scope 1 ~3,7 Mt CO2e, Scope 2 ~9,6 Mt CO2e, Scope 3 ~125 Mt CO2e (2024); CDP A Leadership 2025; MSCI AA; net-zero 2050; S95F (QD-OLED 55") ha TUV Rheinland Product Carbon Reduction certification (2026 OLED lineup confermato)
- **LG** (OLED evo G5/G6, C5/C6): CDP A-List 2025 (quarto anno consecutivo); MSCI AAA; SBTi approvato; Scope 1+2 target net-zero 2030; emissioni assolute Scope 1+2 non trovate in questa ricerca (dato separato dalla divisione consumer)
- **Sony** (BRAVIA 9, A95L QD-OLED): CDP A-List 2024; MSCI AAA 6 anni consecutivi; SBTi approvato (primo mondiale nel settore consumer durables); net-zero 2040 tutti gli scope; Scope 1+2 net-zero 2030; rinnovabili 40,1% nel 2024 (target 35% superato); Scope 3 -45% entro 2035 (base 2018)
- **TP Vision/Philips OLED+**: CDP B clima, A- acqua; EcoVadis Platinum (corporate); SBTi approvato 2022; Scope 1+2+3 use-phase -42% entro 2030; dati assoluti Scope non trovati pubblicamente; PPDS (divisione professional) ha EcoVadis Gold
- **Panasonic**: CDP A-List 2025 (clima + water security); MSCI AAA (novembre 2025); SBTi verificato per target net-zero 2050; Scope 1 ~316 kt CO2e, Scope 2 ~1.207 kt CO2e, Scope 3 ~124.995 kt CO2e (FY2024); net-zero Scope 1+2 entro 2030 (-90% vs 2019); 45 stabilimenti net-zero CO2 in FY2025; Energy Star Partner of the Year Sustained Excellence 14° anno consecutivo
- **Loewe** (TV tedesco): nessun CDP rating trovato; nessun SBTi; nessun MSCI rating trovato; 100% energia rinnovabile in produzione (dichiarato); produzione 100% Kronach, Germania (supply chain corta); no dati Scope pubblici — azienda privata medio-piccola (~300 dipendenti); rilevante insolvenza 2023, rilevata da Klangheim GmbH

#### Certificazioni prodotto brand premium

- **Samsung QD-OLED (S95F/S95G 55")**: TUV Rheinland Product Carbon Reduction (2026 OLED lineup); TUV Rheinland Product Carbon Footprint; materiali riciclati 31% su plastica (corporate 2024); QLED 75Q60C = 982 kg CO2e ciclo vita (proxy di riferimento per QD-OLED simile); nessun EU Ecolabel o EPEAT consumer trovato
- **LG OLED evo (G5 55", G6 55", C5 55", C6 55")**: Carbon Trust Reducing CO2 (G5 55" e G6 55" confermati; G6 6° anno consecutivo); Intertek Resource Efficiency; E-Cycle Excellent Products Korea; 50% plastica riciclata prevista nel 2025 (aumento da 30% del 2024); stima risparmio 80.000 ton CO2 e 15.000 ton plastica nel 2026 vs LCD equivalente; EU Energy Label D per 77"/83" C6
- **Sony BRAVIA 9 / A95L QD-OLED**: SORPLAS 65% sul rear cover (BRAVIA 9); riduzione CO2 produzione plastica -72% vs vergine; Material-to-Material recycling (rear cover dismessi → nuovo SORPLAS dal 2025); Energy Star su modelli principali USA; nessun EU Ecolabel trovato specificamente su OLED premium
- **Philips OLED+ 910 / OLED+ 908 55"**: piedi in alluminio riciclato confermati; packaging in transizione plastica-free; nessuna certificazione prodotto specifica trovata (EPEAT, Energy Star, Carbon Trust) per OLED+ line; iF Design Award 2025 (non eco-specifico)
- **Panasonic Z95B / Z90B 55"**: nessuna certificazione prodotto eco specifica trovata per questi modelli (né Energy Star, né EU Ecolabel, né Carbon Trust, né TUV); a livello corporate Panasonic riceve Energy Star sustained excellence; ha programma PETEC (20M elettrodomestici riciclati dal 2001); circolarità materiali dichiarata (metalli, plastiche riciclate in design); gap: nessun carbon footprint per unità pubblicato
- **Loewe Iconic / Loewe Stellar**: Syno-Stone (materiale minerale da risorse riciclate locali, riciclabile) — unico brand a usare materiali non-plastici nel corpo TV; 10 anni di ricambi garantiti; software update a lungo termine; 100% energia rinnovabile in produzione; NO certificazioni terze verificabili trovate (EPEAT, Energy Star, EU Ecolabel, Carbon Trust, TUV)

#### Modelli premium 55" disponibili sul mercato italiano (giugno 2026)

- **Samsung S95F 55" QD-OLED** — ~1.800-2.200€ (prezzo stimato 2025)
- **LG G6 55" OLED evo MLA** — ~2.000-2.500€
- **LG C6 55" OLED evo** — ~1.200-1.500€
- **Sony BRAVIA 9 55" (Mini LED)** — ~1.800-2.500€
- **Sony A95L 55" QD-OLED** — ~2.500-3.500€ (modello 2023, ancora disponibile)
- **Philips OLED+ 910 55"** — ~1.500-2.000€ (da giugno 2026)
- **Panasonic Z95B 55" OLED** — ~1.800-2.500€
- **Loewe Stellar / Iconic 55"** — ~3.000-5.000€

#### Ranking sostenibilità fascia premium

1. **Sony** — CDP A-List, MSCI AAA, SBTi primo mondiale settore, SORPLAS 65% rear cover con closed-loop, net-zero 2040 — il più credibile e verificabile
2. **Panasonic** — CDP A-List 2025 (clima + water), MSCI AAA, SBTi verificato, Scope 1+2+3 tutti pubblicati, 45 stabilimenti net-zero, Energy Star 14 anni — corporate eccellente ma nessuna certificazione prodotto TV specifica trovata
3. **LG** — CDP A-List, MSCI AAA, Carbon Trust Reducing CO2 su G5/G6 55", 50% recycled plastic target 2025, risparmio OLED vs LCD documentato — ottimo a livello prodotto
4. **Samsung QD-OLED** — CDP A, MSCI AA, TUV Carbon Reduction su OLED lineup, 31% recycled plastic, Scope 3 125 Mt (tra i più alti assoluti) — buono ma controversia DS Division pesa; greenwashing risk su Q60/Q65 base (non premium)
5. **TP Vision/Philips OLED+** — CDP B/A-, EcoVadis Platinum, SBTi, ma zero certificazioni prodotto specifiche trovate su OLED+; piedi alluminio riciclato unica evidenza prodotto-specifica
6. **Loewe** — approccio genuino (energia rinnovabile, supply chain locale, Syno-Stone, 10 anni ricambi) ma zero CDP, zero SBTi, zero certificazioni terze verificabili su prodotto; azienda piccola post-insolvenza 2023 — credibilità limitata dalla mancanza di audit indipendenti

#### Note greenwashing fascia premium

- **Panasonic**: forte a livello corporate ma trasparenza prodotto TV quasi assente — rischio di "sustainability washing by proxy" (si vende la reputazione corporate senza certificazioni di prodotto)
- **Loewe**: narrazione "Made in Germany + longevity" convincente ma non verificabile da terzi; nessun CDP, nessun SBTi, nessun report pubblico emissioni — filosofia credibile, dati assenti
- **Philips OLED+**: EcoVadis Platinum è corporate (TP Vision), non specifico OLED+ — gap tra comunicazione e dati prodotto
- **Sony**: il più integro — SORPLAS verificabile chimicamente, Material-to-Material documentato, CDP A-List, SBTi approvato — basso rischio greenwashing
- **Samsung**: attenzione al marketing TUV su OLED (giustificato) vs QLED base (non coperto) — premium QD-OLED OK, non estendere claim a tutta la gamma

### Greenwashing alert per categoria TV
- **Samsung QLED base (Q60/Q65)**: certificazioni TÜV 2026 non coprono questi modelli — solo OLED e Micro RGB hanno Carbon Reduction. I Q60/Q65 hanno meno trasparenza ambientale a livello di prodotto specifico. Rilevante: scoperto nel 2022 che i Neo QLED riconoscevano i test benchmark (rimosso dopo controversia). Segnala disallineamento marketing/realtà.
- **Hisense**: claim "green revolution" e "lighthouse factory" ben documentati WEF, ma nessun Scope 3 supply chain pubblicato dettagliatamente — prudenza; carbon peaking 2026 non ancora verificabile
- **TCL**: S&P ESG 1/100 è un segnale datato; EcoVadis Gold 80/100 (2025) più recente e credibile; ISO 14067 su 33 prodotti positivo; Scope 3 mai dichiarato è il gap principale
- **Samsung DS Division** (semiconductors): controversia concreta su nuovo complesso Yongin (10GW consumo, 3GW da LNG) — non impatta direttamente TV DX Division ma segnala disallineamento interno
- **Sony** è il più credibile in assoluto (CDP A-List, SBTi approvato, MSCI AAA 6 anni consecutivi, SORPLAS verificabile) ma i QLED non sono nel portfolio Sony — Sony fa solo LCD entry e OLED premium
- **TP Vision/Philips**: EcoVadis Platinum, CDP B/A-, SBTi — credibile; meno visibilità su prodotto specifico QLED
