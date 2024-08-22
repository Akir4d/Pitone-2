def media_mobile(lista, n):
    risultato = []
    for i in range(len(lista)):
        if i < n - 1:
            al = i + 1 # per lo slicing fino ad "al"
            media = sum(lista[:al]) / (i + 1)
        else:
            dal = i - n + 1 # slicing "dal"
            al = i + 1 # per lo slicing fino ad "al"
            media = sum(lista[dal:al]) / n
        risultato.append(media)
    return risultato

#Test
numeri = [1,2,3,4,5,6,7,8,9,10]
print(numeri[:2])
print(numeri[3:7])
n = 3
print(media_mobile(numeri, n))