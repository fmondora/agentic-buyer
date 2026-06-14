# Safety Gate / RAPEX — Playbook di navigazione

## Come funziona
Safety Gate (ex RAPEX) e il sistema di allerta rapida dell'Unione Europea per prodotti di consumo non alimentari pericolosi. Quando un prodotto viene richiamato o segnalato come pericoloso in un paese EU, l'alert viene pubblicato su Safety Gate e condiviso con tutti gli stati membri.

## Portale pubblico
- URL: `https://ec.europa.eu/safety-gate-alerts/screen/webReport`
- Accesso: gratuito, nessuna registrazione
- Ricerca per: brand, categoria, paese notificante, tipo di rischio

## Strategia di ricerca

### 1. Ricerca per brand
WebSearch:
```
site:ec.europa.eu/safety-gate "[brand]" product recall
```

### 2. Ricerca per categoria
WebSearch:
```
site:ec.europa.eu/safety-gate "[categoria]" alert [anno]
```

### 3. Dataset OpenDataSoft (dati strutturati)
Dataset RAPEX completo su OpenDataSoft:
```
WebFetch: https://public.opendatasoft.com/explore/dataset/healthref-europe-rapex-en/table/?q=[brand]
```
Contiene: brand, categoria, tipo difetto, paese, data, misure adottate, livello rischio.

### 4. Ricerca per modello specifico
WebSearch:
```
"safety gate" OR "RAPEX" "[brand] [modello]" recall alert
```

## Dati estraibili per il BrandRater

1. **Numero totale di alert** per brand — indicatore di problemi ricorrenti
2. **Gravita degli alert** — rischio serio vs rischio medio
3. **Tipo di difetto** — elettrico, chimico, meccanico, incendio
4. **Misure adottate** — richiamo volontario vs forzato dalle autorita
5. **Trend temporale** — alert in aumento o diminuzione negli ultimi anni
6. **Confronto tra brand** — chi ha piu richiami nella stessa categoria

## Categorie coperte
- Elettronica di consumo (TV, caricatori, batterie, cavi)
- Elettrodomestici (lavatrici, asciugacapelli, tostapane)
- Giocattoli
- Abbigliamento e tessili
- Cosmetici
- Mobili
- Veicoli e accessori

**Non copre**: alimenti, farmaci, dispositivi medici (hanno sistemi di alert separati)

## Interpretazione per il BrandRater

| Alert | Interpretazione |
|-------|----------------|
| 0 alert recenti | Positivo — nessun prodotto richiamato |
| 1-2 alert in 3 anni | Nella norma — incidenti isolati possibili per qualsiasi brand |
| 3-5 alert in 3 anni | Attenzione — pattern di problemi qualita |
| 5+ alert in 3 anni | Red flag — problemi sistematici di qualita/sicurezza |

Nota: i brand con volumi di vendita altissimi (Samsung, LG) hanno piu probabilita statistica di alert. Normalizzare per volume di mercato stimato.

## Limitazioni
- Non tutti i richiami passano per Safety Gate — alcuni sono gestiti direttamente a livello nazionale
- I dati su OpenDataSoft possono avere un ritardo di aggiornamento
- Safety Gate copre solo prodotti consumer, non B2B/professionali
- Non indica il numero di unita vendute, quindi non permette di calcolare il tasso di difetto

## Note
- Safety Gate e la fonte piu autorevole EU per richiami prodotto — piu affidabile di database nazionali singoli
- Un brand con zero alert Safety Gate in 3+ anni ha un segnale positivo forte
- Cercare anche su CPSC (USA): `site:cpsc.gov "[brand]" recall` — i richiami USA spesso anticipano quelli EU
