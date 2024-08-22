import socket as soc

SRV_ADDR = ""
SRV_PORT = 44444

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
address = (SRV_ADDR, SRV_PORT)
s.bind(address)
s.listen(1)
print(f"Il servizio e' avviato: attendo connessioni in entrata su {SRV_PORT}")
connection, addressClient = s.accept()
print("Sono connesso con l'indirizzo:", addressClient)
while True:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b"-- Messaggio ricevuto! --\n")
    print(data.decode("UTF-8"))
connection.close()