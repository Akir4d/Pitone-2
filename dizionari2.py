dizionario = {'nome': 'Alice', 'età': 31, 'città': 'Roma', 'email': 'alice@example.com'}

print(dizionario.values())
for i in dizionario.values():
    print(i)

print(dizionario.keys())
for i in dizionario.keys():
    print(i)

dizionario["occhi"] = "castani"
print(dizionario)

for key, value in dizionario.items():
    print(key, value)

for item in dizionario.items():
    print(item)