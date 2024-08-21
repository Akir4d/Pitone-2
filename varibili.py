"""
Variabili in python

non devono mai iniziare per numero
possono contenere lettere a-z e A-Z
sono case-sensitive ovvero le lettere
maiuscole vengono considerate diverse 
dalle minuscole, ovvero:
Paolo = 1
e' diverso da
paolo = 1
"""

# le varibili sono a tipo dinamico (non tipizzato)
variabile_1 = 1

# le varibili si tipizzano in base all'assegnazione
print(variabile_1)
# cio' significa che le variabili posso essere riassegnate 
# come tipologia
variabile_1 = "ciao"
# Questa pratica e' lecita ma sconsigliata
print(variabile_1)

# tipi di dati
# int numero intero senza decimale es
x=10
# In virgola mobile float
y=3.14
# Stringa -> str
nome = "Alice"
# Boleano (bool)
utente_attivo = True
# List (list)
numeri = [1, 2, 3, 4, 5] # gli elementi possono cambiare
numeri[2] = 10
print(numeri)
# Tuple (tuple)
coordinate = (10, 20) # gli elemnti non possono cambiare
# coordinate[0] = 12 # questo provoca un errore
print(coordinate[0])
# Dizionario (dict)
utente = {"nome": "Alice", "eta": 25}
print(utente["nome"])