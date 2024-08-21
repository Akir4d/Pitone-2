"""
< Minore di 
<= Minore o uguale 
== Uguale 
> Maggiore di 
>= Maggiore o uguale 
!= Diverso 
is/is not Identità dell'oggetto / negazione 
in/not in E' contenuto / non è contenuto 
and AND logico 
or OR logico 
not NOT logico
"""
x = 10
y = int(input("Inserisci y: "))

if x < y:
    print("x e' minore di y")
else:
    print("x e' maggiore o uguale a y")
frutta = ["banana", "pera", "pesca"]
chefrutta = input("frutta: ")
if chefrutta.lower() in frutta:
    print(f"Abbiamo {chefrutta}")
else:
    print(f"Non abbiamo {chefrutta}")
