numero = 10

def somma(x, y):
    print(f"Sommo {x} a {y}")
    return x + y

def benvenuto():
    global numero
    numero = 20
    print(f"Ciao ti do il benvenuto {numero}")

benvenuto()
s = somma(23, 67)
print(s)
print(numero)
print(somma(y=23, x=90))