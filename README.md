# Quantum Broker con politiche di dispatch
## Funzionamento
Nella richiesta l'utente specifica una lista di politiche per il filtraggio della distribuzione nel campo "policies". Ogni politica è definita tramite il nome ed il livello (es. "lowcost-50"), più è alto il livello e più sarà marcato il filtraggio. I livelli vanno da 1 a 99, questo numero rappresenta la percentuale di dispatch che verranno eliminate. Le varie politiche vengono implementate secondo l'ordine nella lista della richiesta ed ogni politica con relativo livello fa riferimento ai dispatch restituiti dalle politiche precedenti.
## File aggiunti:
- icsoc_parser/policies.py
- icsoc_parser/policies_handler.py
## File modificati
- icsoc_parser/qbroker-asp.py
- icsoc_parser/asp/request_parser.py
- icosc_parser/requests/usecase.json
## policies.py
Si occupa dell'implementazione delle varie politiche tramite funzioni omonime che prendono in input una serie di parametri, tra cui la lista dei dispatch generati, e restituiscono una lista di dispatch filtrata secondo la politica utilizzata. Oltre alla lista prendono come input anche "level" che rappresenta il livello per il quale si vuole implementare la politica.
## policies_handler.py
Prende in input la lista dei dispatch generati e la lista delle politiche da utilizzare. Chiama in sequenza le funzioni associate alle politiche, filtrando man mano i dispatch. Restituisce il singolo dispatch migliore.