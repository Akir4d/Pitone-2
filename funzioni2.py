numero = 10

def somma(x, y):
    print(f"Sommo {x} a {y}")
    return x + y

def benvenuto():
    global numero
    numero = 20
    print(f"Ciao ti do il benvenuto {numero}")