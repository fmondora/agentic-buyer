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
