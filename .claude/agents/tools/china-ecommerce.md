# E-commerce cinese — Playbook

## Piattaforme B2C (consumatore finale)

### AliExpress (aliexpress.com)
- **Tipo**: B2C marketplace, venditori cinesi diretti
- **Ricerca**: `site:aliexpress.com "[prodotto]"` o WebSearch `aliexpress [prodotto]`
- **Prezzi**: spesso in USD, convertire in EUR (+2-3% commissione carta)
- **Spedizione IT**: gratuita standard (15-45gg), €3-15 per tracking/speed (7-15gg)
- **IVA**: IOSS pre-pagata (inclusa nel prezzo mostrato per EU)
- **Dazi**: sotto €150 nessun dazio. Sopra €150: dazio per categoria + handling
- **Protezione**: 90gg buyer protection, dispute resolution, rimborso se non arriva
- **Magazzini EU**: alcuni venditori hanno warehouse in Spagna/Francia/Polonia — prioritizzare (consegna 3-7gg, nessun rischio dogana)
- **Rischi**: qualita variabile, foto ingannevoli, size chart diverso da EU, garanzia limitata
- **URL pattern**: `https://www.aliexpress.com/item/[id].html`

### Temu (temu.com)
- **Tipo**: B2C diretto (PDD Holdings, stessa azienda di Pinduoduo)
- **Ricerca**: `site:temu.com "[prodotto]"` o WebSearch `temu [prodotto]`
- **Prezzi**: EUR, gia inclusivi di IVA per EU
- **Spedizione IT**: gratuita 7-15gg (warehouse EU per molti prodotti), express 3-7gg
- **IVA**: IOSS pre-pagata
- **Dazi**: come AliExpress (sotto €150 nessun dazio)
- **Protezione**: 90gg return, rimborso automatico
- **Rischi**: qualita MOLTO variabile, brand dubbi, poca trasparenza su materiali, controversy etiche (lavoro forzato sospetto)
- **Note**: prezzi spesso piu bassi di AliExpress per prodotti generici

### Banggood (banggood.com)
- **Tipo**: B2C diretto, specializzato elettronica/gadget/hobby
- **Ricerca**: `site:banggood.com "[prodotto]"` o WebSearch `banggood [prodotto]`
- **Prezzi**: EUR/USD
- **Spedizione IT**: €3-10, warehouse EU (Spagna, Polonia) 3-7gg
- **IVA**: IOSS per spedizioni CN, inclusa per warehouse EU
- **Protezione**: 30gg return, DOA guarantee
- **Rischi**: assistenza lenta, stock limitato su warehouse EU
- **Note**: buono per droni, RC, componenti elettronici, tool

### DHgate (dhgate.com)
- **Tipo**: B2C/B2B, marketplace
- **Ricerca**: `site:dhgate.com "[prodotto]"`
- **Prezzi**: USD
- **Spedizione IT**: gratuita lenta (20-40gg), €10-30 express
- **IVA**: spesso NON IOSS — rischio tassa alla consegna + handling fee corriere (€5-15)
- **Protezione**: debole rispetto ad AliExpress
- **Rischi**: piu rischi di contraffazione, dispute resolution meno efficace
- **Note**: sconsigliato per primo acquisto, utile per bulk

### Geekbuying (geekbuying.com)
- **Tipo**: B2C diretto, tech/gadget
- **Ricerca**: `site:geekbuying.com "[prodotto]"`
- **Prezzi**: EUR
- **Spedizione IT**: €3-10, warehouse EU disponibile
- **IVA**: IOSS
- **Rischi**: catalogo limitato, assistenza nella media

## Piattaforme domestiche CN (prezzi fabbrica, piu complessita)

### 1688.com (1688.com)
- **Tipo**: B2B domestico cinese (Alibaba Group)
- **Accesso**: serve agente/forwarder (Superbuy, CSSBuy, Pandabuy, Wegobuy)
- **Prezzi**: CNY (yuan), i piu bassi possibili — prezzi fabbrica
- **MOQ**: spesso 1 pezzo per campione, ma alcuni richiedono 2+
- **Spedizione**: via forwarder — costo consolidamento + spedizione internazionale (~€10-30/kg)
- **IVA/Dazi**: a carico del buyer, calcolati su valore dichiarato
- **Ricerca**: WebSearch `1688.com [prodotto in cinese]` o `[prodotto] 1688 taobao agent`
- **Rischi**: tutto in cinese, nessuna protezione buyer diretta, qualita da verificare con foto agente
- **Note**: risparmio 30-70% su AliExpress per lo stesso prodotto. Vale solo per acquisti mirati.

### Taobao (taobao.com)
- **Tipo**: C2C/B2C domestico cinese (Alibaba Group)
- **Accesso**: serve forwarder (Superbuy, Pandabuy, CSSBuy, Wegobuy)
- **Prezzi**: CNY, intermedi tra 1688 e AliExpress
- **Spedizione**: via forwarder (~€10-30/kg)
- **Ricerca**: WebSearch `taobao [prodotto] site:superbuy.com` o `[prodotto] taobao link`
- **Rischi**: come 1688 ma catalogo consumer piu ampio
- **Note**: per prodotti di nicchia non presenti su AliExpress

### Alibaba (alibaba.com)
- **Tipo**: B2B export, accessibile dall'estero
- **Prezzi**: USD, spesso "1 piece" disponibile come campione
- **Spedizione**: quotazione dal venditore, DHL/FedEx 5-10gg (€20-50)
- **MOQ**: variabile, molti accettano 1 pezzo
- **Protezione**: Trade Assurance (escrow)
- **Ricerca**: `site:alibaba.com "[prodotto]"`
- **Note**: utile per confrontare prezzo fabbrica e capire il markup di AliExpress

## Calcolo costo totale verso Italia

### Formula base (B2C con IOSS)
```
Totale = Prezzo mostrato (IVA inclusa) + Spedizione
```
AliExpress, Temu, Banggood, Geekbuying usano IOSS — il prezzo mostrato include gia IVA 22%.

### Formula senza IOSS (DHgate, venditori non registrati)
```
Totale = Prezzo prodotto
       + Spedizione
       + IVA 22% (su prezzo + spedizione)
       + Handling fee corriere (€5-15)
```

### Formula prodotti sopra €150
```
Totale = Prezzo prodotto
       + Spedizione
       + Dazio doganale (% su valore, varia per categoria HS)
       + IVA 22% (su prezzo + spedizione + dazio)
       + Handling fee corriere (€10-20)
```

### Dazi doganali comuni per categoria
| Categoria | Codice HS | Dazio % |
|---|---|---|
| Elettronica di consumo | 8517/8518 | 0-3.7% |
| Wearable/smartwatch | 9102 | 4.5% |
| Fitness tracker (senza display) | 9031 | 0% |
| Abbigliamento/tessili | 61/62 | 12-17% |
| Scarpe | 64 | 8-17% |
| Accessori in plastica | 3926 | 6.5% |
| Giocattoli | 9503 | 4.7% |
| Utensili cucina acciaio | 7323 | 3.5% |
| Mobili | 9403 | 0-5.6% |

### Formula piattaforme domestiche (via forwarder)
```
Totale = Prezzo CNY (converti in EUR, +2% cambio)
       + Costo agente/forwarder (5-10% del prezzo o tariffa fissa ~€3-5)
       + Spedizione internazionale (€10-30/kg, peso volumetrico se ingombrante)
       + Dazio doganale (se applicabile, su valore dichiarato)
       + IVA 22% (su valore + spedizione + dazio)
       + Handling fee corriere (€5-15)
```

## Strategia di ricerca

1. **Prima AliExpress + Temu** — piu accessibili, IOSS, protezione buyer
2. **Poi Banggood/Geekbuying** — se prodotto tech/elettronica, cercare warehouse EU
3. **Poi 1688/Taobao** (via WebSearch) — per capire prezzo fabbrica e margine
4. **Alibaba** — per bulk o confronto prezzi B2B
5. **DHgate** — solo se non trovato altrove, piu rischi

## Red flags (segnalare SEMPRE nel report)
- Prezzo troppo basso rispetto alla media (possibile contraffazione)
- Nessuna review o review solo a 5 stelle (fake)
- Venditori con meno di 6 mesi di attivita
- Prodotti con marchi EU/US a prezzi impossibili (contraffazione certa)
- Specifiche troppo belle per il prezzo (overspec marketing)
- Nessuna certificazione CE/FCC mostrata (rischio sicurezza)
- Spedizione solo da CN senza opzione EU warehouse (tempi lunghi + rischio dogana)

## Confronto con prezzo EU
Per ogni prodotto trovato su piattaforma cinese, SEMPRE confrontare con:
1. Prezzo Amazon IT/DE del prodotto identico o equivalente
2. Prezzo idealo del prodotto identico
3. Se il prodotto e un clone/alternativa, segnalarlo esplicitamente

## Conversione valute
- CNY → EUR: cercare "CNY to EUR" su WebSearch
- USD → EUR: cercare "USD to EUR" su WebSearch
- Aggiungere 2-3% per commissione carta su valute non-EUR
