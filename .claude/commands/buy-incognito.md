---
allowed-tools: WebSearch, WebFetch, Agent, Read, Glob, Bash, AskUserQuestion
---

# /buy-incognito — Acquisto Intelligente in Modalita Incognito

Sei l'orchestratore del sistema Buyer in **modalita incognito**. Funziona esattamente come `/buy` ma **senza lasciare traccia**.

## Regole incognito (NON NEGOZIABILI)

1. **NON salvare report su disco** — niente Write in `reports/`
2. **NON aggiornare learnings** — niente Edit/Write in `.claude/agents/learnings/`
3. **NON aggiornare la memoria** — niente Write/Edit su MEMORY.md
4. **NON menzionare il prodotto** in nessun file persistente
5. **Il risultato esiste SOLO nella conversazione** — dopo `/clear` non resta traccia
6. **Gli agenti NON hanno il tool Write/Edit** — passagli solo Read, WebSearch, WebFetch, Glob

IMPORTANTE: Nota che `allowed-tools` sopra NON include Write e Edit. Questo comando non puo scrivere file.

## Flusso

Identico a `/buy` ma con queste differenze:

### Step 1: Parsing
Come `/buy`. Analizza: `$ARGUMENTS`

### Step 2: Discovery
Come `/buy`, in foreground.

### Step 3: Lancia i 7 agenti
Come `/buy`, in parallelo e background (7 agenti, senza StrategicBuyer). Nel prompt di ogni agente aggiungi:
> **MODALITA INCOGNITO**: NON aggiornare i learnings. NON scrivere su nessun file. Solo ricerca e output testuale.

### Step 4: StrategicBuyer (sequenziale)
Come `/buy`, lancia lo StrategicBuyer in foreground dopo che i 7 agenti hanno completato. Passagli i risultati dei 7 agenti. Aggiungi al prompt:
> **MODALITA INCOGNITO**: NON aggiornare i learnings. NON scrivere su nessun file. Solo ricerca e output testuale.

### Step 5: Raccogli e sintetizza
Come `/buy`, ma il report viene presentato SOLO in conversazione, mai salvato su disco.

### Step 6: Presenta il verdetto
Come `/buy`, ma invece di "Link al report completo" scrivi:
> Modalita incognito: il report non e stato salvato. Usa `/clear` per eliminare ogni traccia dalla conversazione.

## Conferma iniziale

Prima di partire, mostra all'utente:
```
Modalita incognito attiva:
- Nessun report salvato su disco
- Nessun learnings aggiornato
- Nessuna traccia in memoria
- Il risultato esiste solo in questa conversazione
```

Poi procedi con la ricerca.
