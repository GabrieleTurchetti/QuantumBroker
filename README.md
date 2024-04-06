# Quantum Broker con Politiche
## Politiche
I dispatch generati dall'ASP vengono filtrati in base a una lista di politiche definite nella sezione "policies" della richiesta. Esistono 2 tipi di politiche che è possibile specificare:
1. Politiche Custom
2. Politiche Standard
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

Le metriche fungono da parametro di confronto nella selezione del dispatch ideale, il peso ne indica l'importanza (se il peso e' negativo vengono svantaggiati i dispatch con il valore di quella metrica alto). Le metriche utilizzabili possono essere delle metriche standard o metriche custom create direttamente nella sezione "metrics" della richiesta. Le metriche standard sono:
- total_cost
- total_energy_cost
- total_time
- used_computers
- shots_difference

Il livello invece definisce la percentuale di dispatch da scartare, lasciando solo il (100 - "level")% dei dispatch migliori. La valutazione dei dispatch è definita dalla seguente equazione:

    value = nome_metrica1 * peso_metrica1 + nome_metrica2 * peso_metrica2 + ... + nome_metricaN * peso_metricaN

Se dopo aver applicato tutte le politiche il numero di dispatch è > 1 allora in automatico viene applicata la politica

    {
        "metrics": {
            total_cost: -1,
            total_energy_cost: -1,
            total_time: -1,
            used_computers: 1,
            shots_difference: -1
        },
        "level": 1
    }

in modo che tra i dispatch rimanenti venga selezionati uno con una valutazione generale migliore.

### Politiche Strandard
Le politiche standard sono definite da:

    nome_politica-livello

Di seguito la lista delle politiche standard:
- cost-aware
- time-aware
- reliable
- green

Anche in questo caso se il numero di dispatch dopo aver applicato tutte le politiche è > 1 si procede come per le politiche custom.

Il codice che gestisce le politiche è presente nella cartella "icsoc_parser/policies". Nello specifico il file "policies_manager.py" si occupa della validazione e dell'applicazione in sequenza di tutte le politiche.

## Flusso di Esecuzione di una Richiesta
L'invio di una richiesta parte dal main di "icsoc_parser/qbroker-asp.py". Da qui, nella funzione "policy", viene scritto nel file "program.lp" il codice parsato in codice ASP della richiesta. Nello specifico, per quanto riguarda il codice ASP del circuito, esso viene generato in questa maniera:
1. Viene chiamata la funzione "parse_circuit" di "icsoc_parser/asp/circuit_parser.py".
2. Vengono ottenuti i circuiti compilati per ogni compilatore e per ogni quantum computer tramite la funzione "brokering" di "src/components/qbroker.py", la funzione stessa ritorna solo un circuito compilato per ogni quantum computer, ovvero quello con una profondità minore.
3. A questo punto ad ogni circuito viene assegnato un identificatore e salvato nella cartella "circuits"
4. Infine per ogni circuito viene fatto il parsing in codice ASP tramite la funzione "parse_circuit" di "src/qbroker_asp.py"

Dopo aver ottenuto tutte le regole e fatti ASP, vengono generati tutti i dispatch possibili per poi selezionarne solo uno in base alle politiche definite. A questo punto vengono generati gli oggetti necessari per poter inviare la richiesta effettiva alle varie piattaforme cloud per i quantum computer. Quest'ultima parte viene svolta dal metodo "run" della classe "QBroker" di "icsoc_parser/qbroker.py".