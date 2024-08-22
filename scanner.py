import socket as so

target = input("Dammi l'ip della macchia da scansire: ")
portrange = input("Inserisci un port range (es 5-200): ")
lowport = 5
highport = 200
if "-" in portrange:
    lowport = int(portrange.split('-')[0])
    highport = int(portrange.split('-')[1])

print("Scansisco host:", target, "dalla porta", lowport, "alla porta", highport)
chiuse = []
for port in range(lowport, highport+1):
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("*** Porta", port, "- Aperta ***")
    else:
        chiuse.append(port)
    s.close()

print("Porte chiuse:", chiuse)
