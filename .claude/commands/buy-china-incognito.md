---
allowed-tools: WebSearch, WebFetch, Agent, Read, Glob, Bash, AskUserQuestion
---

# /buy_china_incognito — Acquisto Cinese in Modalita Incognito

Sei l'orchestratore del sistema Buyer in **modalita China + incognito**. La pipeline e **identica** a `/buy_china` ma **senza lasciare traccia su disco**.

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

**Identico a `/buy_china`** in ogni step. L'unica differenza e che nulla viene scritto su disco.

### Step 1: Parsing
Come `/buy_china`. Analizza: `$ARGUMENTS`

### Step 2: Discovery
Come `/buy_china`, in foreground.

### Step 3: ScoutChina (foreground)
Come `/buy_china`. Aggiungi al prompt:
> **MODALITA INCOGNITO**: NON aggiornare i learnings. NON scrivere su nessun file. Solo ricerca e output testuale + JSON strutturato.

### Step 4: Lancia i 9 evaluator (parallelo)
Come `/buy_china`, 9 agenti in parallelo e background. Nel prompt di ogni agente aggiungi:
> **MODALITA INCOGNITO**: NON aggiornare i learnings. NON scrivere su nessun file. Solo ricerca e output testuale + JSON strutturato.

### Step 5: Aggiorna l'utente
Come `/buy_china`.

### Step 6: Sintetizza (senza salvare)
Come `/buy_china` Step 6, ma:
- **NON creare** la directory `tracker/results/`
- **NON salvare** nessun file
- Calcola i punteggi in memoria e usali per il report
- Il report viene presentato SOLO in conversazione

### Step 7: Genera il report (senza salvare)
Come `/buy_china` Step 7, ma il report viene mostrato in conversazione, non salvato.

### Step 8: Presenta il verdetto
Come `/buy_china` Step 8, ma invece di link a file scrivi:
> Modalita incognito: nessun file salvato. Usa `/clear` per eliminare ogni traccia dalla conversazione.

## Conferma iniziale

Prima di partire, mostra all'utente:
```
Modalita China + incognito attiva:
- Ricerca su piattaforme cinesi (AliExpress, Temu, Banggood, 1688, Alibaba)
- Nessun report salvato su disco
- Nessun risultato strutturato salvato
- Nessun learnings aggiornato
- Il risultato esiste solo in questa conversazione
```
