lista = [1, "Ciao", 3.14, [1,2,3], {"nome": "Chiara", "cognome": "Black"}]

print(lista[0])
# se voglio stampare elemento 1 del elemento 3?
print(lista[3][1])
print(lista)
del lista[4]["cognome"]
lista[2] = 1.7777
lista.append("Mi sono appeso")
lista.insert(3, "Mi sono imbucato")
print(lista)
lista.pop()
lista.pop()
lista.remove(1)
lista.remove("Ciao")
del lista[0]
for i in lista:
    print(i)