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
y = 0
while y != 99:
    y = int(input("Premi \n1 per le offerte\n2 per il sevizio marketing\n3 per assistenza \nscegli bene: "))
    if y == 1:
        print("Consulti il sito")
    elif y == 2:
        print("Buongiorno siamo qui per fregarla!")
    elif y == 3:
        print("Abbiamo licenziato tutti i tecnici")
    elif y == 99:
        print("Bene hai trovato il menu' segreto")
    else:
        print(f"Ha appena prelevato {y*10} euro dalla sua carta")
