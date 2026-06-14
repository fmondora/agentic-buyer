# Indice de Reparabilite / Durabilite (Francia) — Playbook di navigazione

## Come funziona
La Francia ha reso obbligatorio dal 1 gennaio 2021 un **indice di riparabilita** (0-10) visualizzato al punto vendita per diverse categorie di prodotti. Dal **gennaio 2025**, per i televisori l'indice e stato sostituito dall'**indice de durabilite** (indice di durabilita), piu completo.

## Differenza reparabilite vs durabilite
- **Reparabilite** (2021-2024 per TV): valuta solo facilita di riparazione (documentazione, ricambi, prezzo ricambi, smontaggio)
- **Durabilite** (2025+ per TV e lavatrici): include riparabilita + affidabilita + robustezza + upgradabilita software

## Fonti dati

### 1. data.gouv.fr (open data ufficiale)
I produttori pubblicano i dati su data.gouv.fr:
```
WebSearch: site:data.gouv.fr "indice de reparabilite" [brand]
```
oppure:
```
WebSearch: site:data.gouv.fr "indice de durabilite" [brand] televiseur
```
Formato: CSV/JSON con score per criterio e score complessivo.

### 2. indicereparabilite.fr
Database aggregato consultabile:
```
WebFetch: https://www.indicereparabilite.fr/etiquette-produit/[brand]/
```
Lista paginata per brand. Contiene score, dettaglio criteri, modello.

### 3. Spareka.fr
Aggregatore indipendente dei punteggi:
```
WebSearch: site:spareka.fr "indice de reparabilite" [brand] [modello]
```

### 4. lcd-compare.com
Lista TV con score riparabilita >= 7, ordinata per dimensione:
```
WebSearch: site:lcd-compare.com "indice de reparabilite" [modello]
```

## Categorie coperte

### Indice de reparabilite (attivo)
- Smartphone
- Laptop
- Aspirapolveri
- Lavastoviglie
- Idropulitrici
- Lavatrici carica dall'alto

### Indice de durabilite (dal 2025)
- **Televisori** (dal 8 gennaio 2025)
- **Lavatrici** (dal 8 aprile 2025)

## Criteri di valutazione (durabilite TV)

| Criterio | Peso | Cosa misura |
|----------|------|-------------|
| Documentazione | 10% | Manuali, schemi riparazione disponibili gratuitamente? |
| Smontabilita | 20% | Facilita apertura, attrezzi necessari, design modulare |
| Disponibilita ricambi | 25% | Ricambi disponibili? Per quanti anni? |
| Prezzo ricambi | 20% | Rapporto prezzo ricambio / prezzo prodotto |
| Affidabilita | 12,5% | Resistenza a stress, test di durata, MTBF |
| Upgradabilita software | 12,5% | Aggiornamenti garantiti, anni di supporto |

## Dati estraibili per il LifecycleAdvisor

1. **Score complessivo** (0-10) — confrontabile tra modelli e brand
2. **Score per criterio** — permette di capire DOVE il prodotto e forte/debole
3. **Anni ricambi garantiti** — dato ufficiale dichiarato dal produttore
4. **Prezzo ricambi** — rapporto con prezzo prodotto
5. **Upgradabilita software** — anni di supporto dichiarati

## Score noti per TV (riferimento)
- Samsung QLED: tipicamente 7.5-8.1/10 (tra i migliori)
- Samsung OLED: ~8.0/10 (stimato da pattern simili QLED)
- LG: ~7.0-7.5/10 (stimato)
- TCL, Hisense: score non sempre pubblicati; stimati 6-7/10

## Limitazioni
- Solo prodotti venduti in Francia (ma copre tutti i brand internazionali)
- I dati su data.gouv.fr sono pubblicati volontariamente dai produttori — non tutti lo fanno
- L'indice de durabilite per TV e nuovo (gennaio 2025) — pochi dati accumulati
- Score auto-dichiarati dai produttori (ma verificabili dalle autorita)

## Note
- E l'unico indice di riparabilita/durabilita OBBLIGATORIO PER LEGGE al mondo
- I dati sono open data su data.gouv.fr — ideali per confronto oggettivo
- Dal 2025 la Francia e il benchmark globale: l'UE sta valutando un indice simile EU-wide
