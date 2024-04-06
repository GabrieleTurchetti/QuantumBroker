# Quantum Broker with Dispatch Policies# Quantum Broker con Politiche
## Politiche
I dispatch generati dall'ASP vengono filtrati in base a una lista di politiche definite nella sezione "policies" della richiesta.
### Politiche Custom
Le politiche custom hanno la seguente struttura:

    {
        "metrics": {
            "nome_metrica": peso_metrica1, (da -1 a 1)
            "nome_metrica2": peso_metrica2, (da -1 a 1)
            ...
            "nome_metricaN": peso_metricaN (da -1 a 1)
        },
        "level": livello_politica (da 1 a 99)
    }

Le metriche fungono da parametro di confronto nella selezione del dispatch ideale, il peso ne indica l'importanza (se il peso e' negativo vengono svantaggiati i dispatch con il valore di quella metrica alto). Le metriche utilizzabili possono essere delle metriche standard o metriche custom create direttamente nella richiesta nella sezione "metrics". Le metriche standard sono queste:
- total_cost
- total_energy_cost
- total_time
- used_computers
- shots_difference

Il livello definisce quanto la politica filtra i dispatch generati. Indica la percentuale di dispatch da non considerare (da 1% a 99%). I dispatch quindi vengono ordinati in base ad un valore. Il valore viene calcolato come combinazione lineare in questra maniera:

    nome_metrica1 * peso_metrica1 + nome_metrica2 * peso_metrica2 + ... + nome_metricaN * peso_metricaN

In seguito vengono selezionati solo i (100 - "livello_politica")% migliori in base a questo valore. Se dopo aver applicato tutte le politiche il numero di dispatch e' > 1 allora in automatico viene applicata la politica

    {
        "metrics": {
            total_cost: -1,
            total_energy_cost: -1,
            total_time: -1,
            used_computers: 1,
            shots_difference: -1
        },
        "level": 99
    }

a ripetizione, fino a che non vi e' un solo dispath come risultato.

### Politiche Strandard
Le politiche standard sono definite da:

    nome_politica-livello

Di seguito la lista delle politiche standard:
- cost-aware
- time-aware
- reliable
- green

Anche in questo caso se il numero di dispatch dopo aver applicato tutte le politiche e' > 1 si procede come per le politiche custom.

Il codice che gestisce le politiche e' presente nella cartella icsoc_parser/policies. Nello specifico il file "policies_manager.py" si occupa della validazione e dell'applicazione in sequenza di tutte le politiche.

## Flusso di Esecuzione di una Richiesta
Il nome del file json contenente la richiesta viene specificato nel codice di "icsoc_parser/qbroker-asp.py". Da qui, nella funzione "policy", viene inserito nel file "program.lp" il codice ASP della richiesta. Nello specifico per quanto riguarda il codice ASP del circuito esso viene generato in questa maniera:
1. Viene chiamata la funzione "parse_circuit" in "icsoc_parser/asp/circuit_parser.py".
2. Vengono ottenuti i circiti compilati per ogni compilatore e per ogni quantum computer tramite la funzione "brokering" del file "src/components/qbroker.py", la funzione stessa ritorna solo un circuito compilato per ogni quantum computer, cioe' quello con una profondita' minore.
3. A questo punto ad ogni circuito viene assegnato un identificativo e salvato nel file "circuits/circuits.json"
4. Infine per ogni circuito viene fatto il parsing in codice ASP tramite la funzione "parse_circuit" del file "src/qbroker_asp.py"

Dopo aver ottenuto tutte le regole e fatti ASP, vengono generati i dispatch possibili per poi selezionarne solo uno in base alle politiche definite. A questo punto vengono generati gli oggetti necessari per poter inviare la richiesta effettiva alle varie piattaforme cloud per i quantum computer. Questo viene svolto nel file "icsoc_parser/qbroker.py".# Quantum Broker con Politiche
## Politiche
I dispatch generati dall'ASP vengono filtrati in base a una lista di politiche definite nella sezione "policies" della richiesta.
### Politiche Custom
Le politiche custom hanno la seguente struttura:

    {
        "metrics": {
            "nome_metrica": peso_metrica1, (da -1 a 1)
            "nome_metrica2": peso_metrica2, (da -1 a 1)
            ...
            "nome_metricaN": peso_metricaN (da -1 a 1)
        },
        "level": livello_politica (da 1 a 99)
    }

Le metriche fungono da parametro di confronto nella selezione del dispatch ideale, il peso ne indica l'importanza (se il peso e' negativo vengono svantaggiati i dispatch con il valore di quella metrica alto). Le metriche utilizzabili possono essere delle metriche standard o metriche custom create direttamente nella richiesta nella sezione "metrics". Le metriche standard sono queste:
- total_cost
- total_energy_cost
- total_time
- used_computers
- shots_difference

Il livello definisce quanto la politica filtra i dispatch generati. Indica la percentuale di dispatch da non considerare (da 1% a 99%). I dispatch quindi vengono ordinati in base ad un valore. Il valore viene calcolato come combinazione lineare in questra maniera:

    nome_metrica1 * peso_metrica1 + nome_metrica2 * peso_metrica2 + ... + nome_metricaN * peso_metricaN

In seguito vengono selezionati solo i (100 - "livello_politica")% migliori in base a questo valore. Se dopo aver applicato tutte le politiche il numero di dispatch e' > 1 allora in automatico viene applicata la politica

    {
        "metrics": {
            total_cost: -1,
            total_energy_cost: -1,
            total_time: -1,
            used_computers: 1,
            shots_difference: -1
        },
        "level": 99
    }

a ripetizione, fino a che non vi e' un solo dispath come risultato.

### Politiche Strandard
Le politiche standard sono definite da:

    nome_politica-livello

Di seguito la lista delle politiche standard:
- cost-aware
- time-aware
- reliable
- green

Anche in questo caso se il numero di dispatch dopo aver applicato tutte le politiche e' > 1 si procede come per le politiche custom.

Il codice che gestisce le politiche e' presente nella cartella icsoc_parser/policies. Nello specifico il file "policies_manager.py" si occupa della validazione e dell'applicazione in sequenza di tutte le politiche.

## Flusso di Esecuzione di una Richiesta
La richiesta, rappresentata da un file json nella cartella "requests", viene letta dal file "icsoc_parser/qbroker-asp.py". Da qui, nella funzione "policy", viene inserito nel file "program.lp" il codice ASP della richiesta. Nello specifico per quanto riguarda il codice ASP del circuito esso viene generato in questa maniera:
1. Viene chiamata la funzione "parse_circuit" in "icsoc_parser/asp/circuit_parser.py".
2. Vengono ottenuti i circiti compilati per ogni compilatore e per ogni quantum computer tramite la funzione "brokering" del file "src/components/qbroker.py", la funzione stessa ritorna solo un circuito compilato per ogni quantum computer, cioe' quello con una profondita' minore.
3. A questo punto ad ogni circuito viene assegnato un identificativo e salvato in un file nella cartella "circuits".
4. Infine per ogni circuito viene fatto il parsing in codice ASP tramite la funzione "parse_circuit" del file "src/qbroker_asp.py".

Dopo aver ottenuto tutte le regole e fatti ASP, vengono generati i dispatch possibili per poi selezionarne solo uno in base alle politiche definite. A questo punto vengono generati gli oggetti necessari per poter inviare la richiesta effettiva alle varie piattaforme cloud per i quantum computer. Questo viene svolto nel file "icsoc_parser/qbroker.py". Una volta ottenuti i risultati viene calcolata la distribuzione in percentuale e inseriti i risultati in un file nella cartella "results".