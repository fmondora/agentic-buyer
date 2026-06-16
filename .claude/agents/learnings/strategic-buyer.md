# Learnings — StrategicBuyer

## Fonti affidabili
- **idealo storico**: API JSON `price-chart/sites/{siteId}/products/{pid}/history?period=3M` — prezzi in centesimi, dividi per 100
- **idealo internazionale**: API HTML fragment `offerpage/fragment/internationalprices/products/{pid}`
- **CamelCamelCamel**: HTML tables con storico Amazon. Cloudflare blocca urllib → usare WebSearch. Chart PNG sempre accessibili
- **trovaprezzi**: API `price_chart/{slug}` — storico prezzi, ma DataDome puo bloccare. Fallback: HTML scraping funziona

## Fonti problematiche
- CamelCamelCamel via fetch diretto: Cloudflare 403. Usare solo WebSearch + chart URL
- trovaprezzi price_chart API: DataDome blocca spesso. Il dato storico viene dal HTML scraping come fallback

## Pattern stagionali noti
- Samsung TV: forte calo 3-6 mesi dopo lancio. Lancio EU tipicamente marzo-aprile
- Samsung QN85F 55": listino ~799€, minimo storico idealo 649€, pagato 599€ (sotto minimo storico) — giugno 2026
- Samsung S95F 55": listino 2.499€, pagato 1.180€ (-52%) — giugno 2026. QD-OLED forte calo nel primo anno
- Prime Day (giugno/luglio): sconto 15-40% su elettronica Amazon
- Black Friday (4o venerdi novembre): sconto 20-50% su tutto, specie TV

## Note per categoria
### TV
- I modelli 2025 calano significativamente entro 6 mesi dal lancio EU
- Samsung non fa mai Dolby Vision — scelta commerciale, non tecnica
- I modelli a fine ciclo possono calare drasticamente o sparire dallo stock
- Confrontare sempre prezzo IT vs DE su idealo — spesso DE e piu economico

### Wearable / Fitness Tracker
- Fitbit Charge 6: modello 2023, prezzo idealo IT oscillante tra €84-127 (volatilita alta). Minimo storico €84,90 raggiunto giugno 2026
- Fitbit Air: lanciato 26 maggio 2026 a €99,99 fisso — troppo nuovo per avere storico significativo
- Amazfit Helio Strap: lanciato giugno 2025 a €99,90, prezzo stabile €99,90-99,99 in EU. Helio Strap 2 confermato per H2 2026 (FCC filing aprile 2026)
- WHOOP: modello subscription-only. Piano One €199/anno, Peak €239/anno, Life €359/anno. Sconti: studenti 10%, healthcare 50%, hero discount militari/infermieri. Primo mese gratis per nuovi iscritti
- Garmin Vivosmart 6: leak confermano GPS integrato, prezzo stimato $149-179, lancio atteso H1-H2 2026 ma non ancora annunciato ufficialmente
- Prime Day (23-26 giugno 2026): forte su fitness tracker, sconti 15-40% tipici su Fitbit e Garmin
- Fitbit Charge 7 non annunciato — Fitbit Air ha preso il posto come novita 2026, Charge 7 forse 2027
- I wearable calano tipicamente a fine anno (Black Friday, Cyber Monday) con sconti 20-40%
