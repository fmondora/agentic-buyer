# Trovaprezzi.it — Playbook di navigazione

## Come funziona
Trovaprezzi e un comparatore prezzi italiano. Aggrega offerte da centinaia di negozi online italiani.

## Strategia di ricerca

### 1. Ricerca prodotto
WebSearch con query:
```
site:trovaprezzi.it "[nome prodotto]"
```

Oppure WebFetch diretto:
```
https://www.trovaprezzi.it/prezzi_[categoria].aspx?libera=[query+url+encoded]
```

Categorie comuni:
- `prezzi_cuffie.aspx` — cuffie e auricolari
- `prezzi_televisori.aspx` — TV
- `prezzi_notebook.aspx` — portatili
- `prezzi_smartphone.aspx` — telefoni
- `prezzi_lavatrici.aspx` — lavatrici
- `prezzi_frigoriferi.aspx` — frigoriferi

Se non conosci la categoria, usa la ricerca generica:
```
https://www.trovaprezzi.it/cerca?q=[query+url+encoded]
```

### 2. Estrazione dati
Dalla pagina risultati, per ogni offerta cerca:
- Nome prodotto completo
- Prezzo (sempre IVA inclusa)
- Nome negozio
- Costo spedizione (spesso indicato accanto al prezzo)
- Disponibilita

### 3. Vantaggi Trovaprezzi
- Mostra TUTTI i negozi che vendono lo stesso prodotto in un'unica pagina
- Include negozi piccoli italiani non presenti su Amazon/eBay
- Prezzi aggiornati frequentemente
- Include costo spedizione nella comparazione

### 4. Limiti
- Solo negozi italiani
- Alcuni negozi piccoli potrebbero avere servizio clienti scarso
- Verificare sempre l'affidabilita del negozio (stelle/recensioni su Trovaprezzi stesso)

## Note
- Se WebFetch non restituisce dati utili (pagina JS-heavy), segnala nel learnings e usa i risultati WebSearch
- I prezzi su Trovaprezzi sono generalmente affidabili e aggiornati
