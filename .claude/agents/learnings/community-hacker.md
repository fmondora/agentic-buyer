# CommunityHacker — Learnings

## Fonti affidabili
- **GitHub search**: `[brand] + api OR library OR reverse OR hack` — risultati diretti
- **Reddit r/quantifiedself**: community attiva su data extraction da wearable
- **Hacker News**: cerca via `hn.algolia.com/api` per risultati strutturati
- **Home Assistant Community**: forum.home-assistant.io per integrazioni IoT

## Fonti problematiche
- **Zepp Health**: nessuna API cloud pubblica, nessun export nativo granulare — solo Health Auto Export (iOS) come workaround
- **Fitbit legacy API**: shutdown settembre 2026, Google Health API richiede scope "Restricted" con review obbligatoria
- **Garmin SSO**: bot detection aggressiva da marzo 2026, ha rotto garth e python-garminconnect temporaneamente

## Pattern di ricerca efficaci
- `"[prodotto] github reverse engineer"` — trova repo specifici
- `"[brand] BLE protocol"` + Gadgetbridge/Codeberg — per wearable BLE
- `"[prodotto] home assistant integration"` — integrazioni IoT
- `"[prodotto] grafana influxdb"` — dashboard self-hosted
- `site:reddit.com [prodotto] hack data export` — community stories (non sempre indicizzato)
- Noop/OpenWhoop/Goose — termini chiave per ecosistema WHOOP open source

## Note per categoria

### Fitness tracker / Wearable (giugno 2026)

#### WHOOP
- API REST ufficiale v2 su developer.whoop.com (OAuth2, webhook, recovery/sleep/workout/cycle)
- **Noop** (NoopApp/noop): app open source Win/Mac/Android, BLE diretto, SQLite locale, NO subscription. Supporta WHOOP 4.0 e 5.0
- **Goose** (b-nnett/goose): Swift/Rust, local-first WHOOP 5.0, protocollo BLE "puffin" documentato (fd4b0001 service family, CRC16-Modbus)
- **OpenWhoop** (bWanShiTong/openwhoop): ~275 stelle, Rust CLI per WHOOP 4.0, no cloud
- **whoop-reader** (christianmeurer): BLE data reader open source per WHOOP 4.0
- **whoop-data** (PyPI): Python library per API interna web app (reverse-engineered)
- **hassio-whoop** (prankstr): Home Assistant integration via HACS
- ToS vietano reverse engineering, ma Noop developer argomenta legalita (no codice Whoop, no DRM bypass)
- InfluxDB+Grafana: guide complete su dev.to (syncing Whoop+Garmin metrics)
- Community tools: kryoseu/whoops (Postgres/MySQL), MyWhoop, Health Auto Export

#### Garmin
- NO API pubblica ufficiale per sviluppatori individuali (solo partner approvati)
- **python-garminconnect** (cyberjunky): 2000+ stelle, 127+ metodi API, usa garth per auth (ora rimpiazzato da native SSO flow)
- **garmin-givemydata** (nrvim): export SQLite + MCP server per AI
- **garmin-connect-export** (pe-st): bulk download FIT/GPX/CSV
- **Home Assistant**: cyberjunky/home-assistant-garmin_connect via HACS, MFA issues con HA 2026.3.2
- **Connect IQ SDK**: Monkey C per app native su device, VS Code extension, ma Vivosmart band potrebbe avere supporto CIQ limitato
- GDPR data export: ZIP completo via garmin.com/account/datamanagement (24-48h), contiene FIT + CSV
- FIT file: granularita al secondo per HR durante attivita
- SSO bot detection aggressiva da marzo 2026, ha rotto temporaneamente tutte le library community

#### Fitbit/Google (Charge 6 + Air)
- Fitbit Web API: shutdown settembre 2026
- **Google Health API**: successore, scope "Restricted" con review obbligatoria, endpoint consolidati
- **google-health-mcp** (davidmosiah): MCP server local-first per Google Health API v4
- **fitbit-cli** (veerendra2): CLI Python con output JSON per AI agents
- **Home Assistant**: integrazione Fitbit esistente, migrazione a Google Health API in discussione (non ancora pronta)
- **IFTTT**: connettore Fitbit attivo (trigger su activity, sleep goals)
- Google Takeout: export JSON, HR aggregato (non al secondo), GDPR compliant
- Export nativo Fitbit: CSV + JSON, max 31 giorni per request
- ATTENZIONE: Google cancella dati Fitbit non migrati il 15 luglio 2026
- Fitbit Air: usa Google Health app (non piu Fitbit app), Health Connect su Android, Apple Health su iOS

#### Amazfit/Zepp (Helio Strap)
- NO API cloud pubblica, NO export nativo granulare
- **Gadgetbridge** v0.90.0+ (marzo 2026): supporto Helio Strap confermato, protocollo Zepp OS, richiede Huami token (pairing iniziale con Zepp app)
- **Amazfit-RE** (wiecosystem): note reverse engineering per dispositivi Amazfit
- **amazfit_pyclient** (MyrikLD): Python client BLE
- **py_amazfit_tools** (ghtalpo): pack/unpack .bin per Amazfit
- Zepp OS SDK: mini app on-device (JavaScript-like), ma NON per data extraction
- Health Auto Export (iOS, $6): workaround via Apple Health per export JSON/CSV
- Zepp app sincronizza con Apple Health / Google Health Connect — unica via di export indiretto
- Repository zepp-health/rest-api su GitHub ma non ufficialmente supportato
- Community molto piu piccola rispetto a Garmin/WHOOP/Fitbit

#### Xiaomi Smart Band (giugno 2026)
- **Gadgetbridge**: Smart Band 10 Pro "Mostly supported" in nightly builds (non ancora release ufficiale), richiede Xiaomi token pairing via vendor app
- **mi-fitness-mac-export** (hayeon17kim): script Python per export SQLite da Mi Fitness macOS → CSV (sleep, HR, steps, workouts)
- **Mi Fitness app**: NO export nativo in-app. Export possibile via account.xiaomi.com (ZIP con CSV: ACTIVITY, HEARTRATE, SLEEP, SPORT)
- **Apple Health sync**: Band 10 Pro ha sync nativo HealthKit (novità 2026), dati HR/sleep/activity sincronizzati
- **Notify for Mi Band**: app Android third-party, VelaJS integration library
- **Python libraries**: felipeq/miband (BLE diretto), miband-HR-python (Band 6/7), python-miio (protocollo miIO/MIoT)
- **Home Assistant**: xiaomi_ble integration nativa per sensori BLE MiBeacon, hass-xiaomi-miot per dispositivi MIoT
- **Versione China vs Global**: China ha NFC transit/payment locale, manca supporto lingue. Global ha multilingual + HealthKit. Gadgetbridge funziona con entrambe
- Community molto attiva su XDA, Reddit, GitHub — ecosistema hacking maturo grazie a generazioni di Mi Band precedenti

#### Huawei Band (giugno 2026)
- **Gadgetbridge**: Band 9 "Mostly supported" (issue firmware 3.1.0.31 rompe pairing), Band 11 Pro "Mostly supported" aggiunto in v0.91.0 (maggio 2026, experimental)
- **Huawei Health Kit**: API REST ufficiale (OAuth2, HMS Core) ma richiede approvazione developer e disponibilità regionale limitata
- **GDPR export**: via account Huawei, ZIP con dati health (formato non standard, JSON nested)
- **Apple Health sync**: Huawei Health sincronizza con HealthKit ma con limitazioni (peso non sincronizza, dati parziali)
- **Health Sync app** (Android only): sincronizza Huawei Health → Strava/Google Fit, storico a pagamento
- **Hitrava** (CTHRU/Hitrava GitHub): converte sport activities Huawei Health → Strava import
- **CCC talk**: "All Your Fitness Data Belongs to You" — reverse engineering Huawei Health Android app, protocollo Huawei Link v2 parzialmente cifrato
- **Home Assistant**: nessuna integrazione specifica per Band, solo huawei_solar e huawei_lte
- **Versione China**: firmware region-locked, NFC WeChat Pay, possibili differenze OTA. Gadgetbridge funziona ma rischio incompatibilità firmware

#### Honor Band (giugno 2026)
- **Gadgetbridge**: Honor Band 9 NON listato nella pagina ufficiale (solo Band 3-7). Usa stesso protocollo Huawei ma non testato
- Honor usa Huawei Health app — stessa situazione di lock-in e stesse limitazioni export
- Honor si è separata da Huawei (2020) ma condivide ancora infrastruttura Health Kit
- Community hacking quasi inesistente — chi hacka Huawei band potenzialmente copre anche Honor, ma nessun progetto specifico

#### JCVital / J-Style (giugno 2026)
- ODM/OEM cinese (jointcorp.com) — produce smartband white-label per terze parti
- SDK e API "disponibili per partner" ma NESSUN repository pubblico, NESSUNA documentazione developer aperta
- ZERO progetti GitHub, ZERO community hacking, ZERO reverse engineering
- App proprietaria, nessun export nativo noto
- Ecosistema completamente chiuso — acquisto solo se si accetta lock-in totale

#### Hume Health (giugno 2026)
- Startup canadese, Band 2.0 — no subscription model (a differenza di WHOOP)
- ATTENZIONE: "Hume AI" (dev.hume.ai) è un'azienda DIVERSA da "Hume Health" (humehealth.com) — non confondere
- Dichiara "raw data export" e sync Apple Health/Google Fit/Garmin/Fitbit
- Reddit community feedback molto negativo: 7 positive vs 14 negative, problemi BT disconnect, dati imprecisi
- NESSUN repository GitHub, NESSUNA API pubblica documentata, NESSUN progetto community
- App proprietaria (iOS/Android), nessun SDK developer
- Lock-in significativo nonostante le dichiarazioni di data portability
