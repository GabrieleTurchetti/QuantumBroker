# Quantum Broker
## Politiche di Spedizione
I dispatch generati dall'ASP vengono filtrati in base a una lista di politiche definite nella sezione "dispatch_policies" della richiesta. Esistono 2 tipi di politiche che è possibile specificare:
1. Politiche Custom
2. Politiche Standard
### Politiche Custom
Le politiche custom hanno la seguente struttura:

    {
        "metric_weights": {
            "nome_metrica": peso_metrica1,
            "nome_metrica2": peso_metrica2,
            ...
            "nome_metricaN": peso_metricaN
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

Se dopo aver applicato tutte le politiche il numero di dispatch è > 1 allora in automatico viene applicata la politica:

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
### Politiche Standard
Le politiche standard sono definite da:

    nome_politica-livello

Di seguito la lista delle politiche standard:
- cost-aware
- time-aware
- reliable
- green

Anche in questo caso se il numero di dispatch dopo aver applicato tutte le politiche è > 1 si procede come per le politiche custom.

Il codice che gestisce le politiche di spedizione è presente nella cartella "icsoc_parser/dispatch_policies". Nello specifico il file "dispatches_manager.py" si occupa della validazione e dell'applicazione in sequenza di tutte le politiche.
## Politiche di Distribuzione
Le politiche che si occupano di elaborare la distribuzione statistica dei risultati sono 2:
- equal: la distrubuzione finale viene calcolata tenendo contro del numero di shots inviati ad ogni computer.
- fair: la distribuzione finale viene calcolata come media delle singole distribuzioni parziali di ogni computer.

Il codice che gestisce le politiche di distribuzione è presente nella cartella "icsoc_parser/dispatch_policies". Nello specifico il file "distribution_manager.py" si occupa della validazione e dell'applicazione in sequenza di tutte le politiche.