# Schema Output Strutturato — JSON Appendice

Ogni agente produce, oltre al markdown narrativo, un **blocco JSON** alla fine del suo output. Questo JSON viene salvato dall'orchestratore in `tracker/results/{date}-{slug}/agents/{agent}.json` e usato per la sintesi automatica.

## Come produrre il JSON

Alla fine del tuo output markdown, aggiungi un blocco fenced:

    ```json:structured-output
    { ... }
    ```

L'orchestratore estrarra questo blocco e lo salvera come file JSON.

## Schema comune

Ogni agente produce un oggetto con:
- `agent`: nome dell'agente (stringa)
- `products`: array di prodotti analizzati

Ogni prodotto ha campi comuni + campi specifici dell'agente:

### Campi comuni (tutti gli agenti)
```json
{
  "name": "Samsung QE55S95F QD-OLED 55\"",
  "brand": "Samsung",
  "model": "QE55S95F",
  "score": 8.5
}
```

- `name`: nome completo prodotto
- `brand`: marca
- `model`: modello (codice produttore)
- `score`: punteggio dell'agente, scala 1-10 (float)

### Campi specifici per agente

#### PriceHunter
```json
{
  "price": 599.00,
  "shipping": 0,
  "total": 599.00,
  "currency": "EUR",
  "url": "https://...",
  "site": "amazon.it",
  "country": "IT",
  "availability": "in_stock",
  "asin": "B0F7LM3M8S",
  "idealo_id": "207213189",
  "trovaprezzi_slug": "samsung_qn85f_55_qe55qn85fauxzt",
  "best_eu_price": {"country": "DE", "price": 579.00, "site": "amazon.de"}
}
```

#### ReviewAnalyst
```json
{
  "rating": 4.3,
  "rating_scale": 5,
  "review_count": 234,
  "sentiment": "positive",
  "strengths": ["colori vivaci", "ottimo contrasto"],
  "weaknesses": ["audio mediocre", "telecomando scomodo"],
  "sources": ["amazon.it", "rtings.com", "youtube"]
}
```

#### SpecComparer
```json
{
  "category": "TV",
  "specs": {
    "panel_type": "QD-OLED",
    "resolution": "4K",
    "size": "55\"",
    "refresh_rate": "144Hz",
    "hdmi_ports": 4
  },
  "energy": {
    "class": "G",
    "kwh_sdr": 108,
    "kwh_hdr": 183,
    "watt_standby": 0.5,
    "source": "EPREL"
  },
  "best_in": ["contrasto", "colori"]
}
```

#### TechnicalCritic
```json
{
  "panel_type": "QD-OLED",
  "contrast_measured": "inf",
  "peak_brightness_nits": 1350,
  "delta_e": 2.1,
  "filmmaker_mode": true,
  "dolby_vision": false,
  "hdr10plus": true,
  "input_lag_ms": 9.5,
  "motion_blur": "low",
  "audio_sufficient": false,
  "verdict": "Eccellente per cinema, audio da integrare"
}
```

#### SustainabilityScout
```json
{
  "energy_class": "G",
  "certifications": ["Energy Star"],
  "cdp_rating": "B",
  "scope1_co2": null,
  "scope2_co2": null,
  "scope3_co2": null,
  "net_zero_target": 2050,
  "b_corp": false,
  "greenwashing_risk": "low",
  "recycled_materials_pct": 20
}
```

#### LifecycleAdvisor
```json
{
  "repairability_fr": 7.2,
  "ifixit_score": null,
  "repair_guides_count": 3,
  "spare_parts": "available",
  "software_support_years": 7,
  "used_value_2y": 400,
  "trade_in_value": 150,
  "warranty_years": 2,
  "obsolescence_signals": []
}
```

#### BrandRater
```json
{
  "tier": "B",
  "reliability": 8,
  "after_sales": 7,
  "territorial_impact": 5,
  "community_impact": 6,
  "ethics": 6,
  "country": "South Korea",
  "production": "Asia",
  "eu_facilities": true,
  "b_corp": false,
  "safety_gate_alerts_3y": 2,
  "controversies": ["TCL QLED lawsuit"]
}
```

#### StrategicBuyer
```json
{
  "verdict": "COMPRA ORA",
  "current_price": 599.00,
  "avg_3m": 689.00,
  "min_historic": 649.00,
  "max_historic": 799.00,
  "trend_30d": "stable",
  "trend_pct": -2.1,
  "volatility": "low",
  "position_vs_avg": "below",
  "position_pct": -13.1,
  "best_eu": {"country": "DE", "price": 579.00},
  "next_event": {"name": "Prime Day", "date": "2026-07", "expected_discount_pct": 15},
  "product_cycle": "mid",
  "new_model_coming": false
}
```

## Regole

1. Se un campo non e disponibile, usa `null` (non omettere il campo)
2. I prezzi sono sempre in EUR (float, 2 decimali)
3. Gli score sono sempre scala 1-10 (float)
4. `verdict` dello StrategicBuyer e sempre una delle 5 stringhe definite
5. `sentiment` del ReviewAnalyst: "positive", "mixed", "negative"
6. `tier` del BrandRater: "A", "B", "C", "D"
7. `availability`: "in_stock", "preorder", "out_of_stock", "limited"
8. `trend_30d`: "rising", "falling", "stable"
9. `product_cycle`: "new", "mid", "end"
10. `spare_parts`: "available", "limited", "unavailable"
