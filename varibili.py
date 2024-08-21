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

# e' possibile convertire un tipo in un altro purche' sia 
# possibile interpretarlo
# posso convertire (cast) 
# str che rappresenta un intero in int
x_str = '10'
x_str = int(x_str)
print(x_str + 1)
# str che rappresenta un float in float
x_str = '9.9'
x_str = float(x_str)
print(x_str + 1.2)
# possiamo convertire un float in int e viceversa
# esiste anche l'insieme (set) in python (per scopi matematici)
# questo puo' essere convertito in lista e viceversa
x_set = {1, 2, 3}
print(x_set)
x_set = list(x_set)
print(x_set)
# stesso discorso si puo' convertire tuple in list e viceversa
x_list = [1, 2, 3]
x_list = tuple(x_list)
print(x_list)
# se dovete converite un float stinga in intero, fate doppio cast
x_float = "9.6"
x_float = int(float(x_float))
print(x_float)

print(f'''Ciao {x_float}
      Mondo''')
print(b"ciao")
