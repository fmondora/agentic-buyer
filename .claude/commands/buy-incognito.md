---
allowed-tools: WebSearch, WebFetch, Agent, Read, Glob, Bash, AskUserQuestion
---

# /buy-incognito — Acquisto Intelligente in Modalita Incognito

Sei l'orchestratore del sistema Buyer in **modalita incognito**. La pipeline e **identica** a `/buy` (stessi step, stessi agenti, stesso flusso) ma **senza lasciare traccia su disco**.

## Regole incognito (NON NEGOZIABILI)

1. **NON salvare report su disco** — niente Write in `reports/`
2. **NON salvare risultati strutturati** — niente Write in `tracker/results/`
3. **NON aggiornare learnings** — niente Edit/Write in `.claude/agents/learnings/`
4. **NON aggiornare la memoria** — niente Write/Edit su MEMORY.md
5. **NON menzionare il prodotto** in nessun file persistente
6. **Il risultato esiste SOLO nella conversazione** — dopo `/clear` non resta traccia
7. **Gli agenti NON hanno il tool Write/Edit** — passagli solo Read, WebSearch, WebFetch, Glob, Bash

IMPORTANTE: Nota che `allowed-tools` sopra NON include Write e Edit. Questo comando non puo scrivere file.

## Flusso

**Identico a `/buy`** in ogni step. L'unica differenza e che nulla viene scritto su disco.

### Step 1: Parsing
Come `/buy`. Analizza: `$ARGUMENTS`

### Step 2: Discovery
Come `/buy`, in foreground.

### Step 3: Lancia i 7 agenti (parallelo)
Come `/buy`, 7 agenti in parallelo e background. Nel prompt di ogni agente aggiungi:
> **MODALITA INCOGNITO**: NON aggiornare i learnings. NON scrivere su nessun file. Solo ricerca e output testuale + JSON strutturato.

Gli agenti producono comunque il blocco `json:structured-output` — i dati restano in memoria di conversazione, non su disco.

### Step 4: Aggiorna l'utente
Come `/buy`.

### Step 5: StrategicBuyer (sequenziale)
Come `/buy`, lancia lo StrategicBuyer in foreground dopo che i 7 agenti hanno completato. Passagli i risultati dei 7 agenti (prodotti, ASIN, idealo_id, prezzi, brand, ciclo prodotto). Aggiungi al prompt:
> **MODALITA INCOGNITO**: NON aggiornare i learnings. NON scrivere su nessun file. Solo ricerca e output testuale + JSON strutturato.

### Step 6: Sintetizza (senza salvare)
Come `/buy` Step 6, ma:
- **NON creare** la directory `tracker/results/`
- **NON salvare** spec.json, agents/*.json, products.json, scores.json
- Calcola i punteggi in memoria e usali per il report
- Il report viene presentato SOLO in conversazione, mai salvato su disco

### Step 7: Genera il report (senza salvare)
Come `/buy` Step 7, ma il report markdown viene mostrato in conversazione, non salvato in `reports/`.

### Step 8: Presenta il verdetto
Come `/buy` Step 8, ma invece di link a file scrivi:
> Modalita incognito: nessun file salvato. Usa `/clear` per eliminare ogni traccia dalla conversazione.

## Conferma iniziale

Prima di partire, mostra all'utente:
```
Modalita incognito attiva:
- Nessun report salvato su disco
- Nessun risultato strutturato salvato
- Nessun learnings aggiornato
- Nessuna traccia in memoria
- Il risultato esiste solo in questa conversazione
```

Poi procedi con la ricerca.
