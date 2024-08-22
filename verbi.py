import http.client

host = input("Inserisci l'host del sistema target: ")
port = input("Inserisci la porta del sistema target: ")
perc = input("Inserisci percorso del sistema target: ")

if port == "": port = 80
if perc == "": perc = '/'

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("OPTIONS", perc)
    response = connection.getresponse()
    print("I metodi abilitati sono: ", response.getheaders(), response.getheader("Allow"))
    connection.close()
except ConnectionRefusedError:
    print("Connessione fallita")