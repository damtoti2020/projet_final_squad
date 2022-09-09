import socket
import subprocess
import sys
from datetime import datetime


subprocess.call('clear', shell=True)

# on va demander a renter l'ip d'un serveur à scanner
remoteServeurIP = input('Entrer l\'IP d\'un serveur à scanner :')

print('-' * 60)
print('lancement du scan des ports dela machine ' + remoteServeurIP)
print('-' * 60)

# pour recuperer le # TEMP:
t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServeurIP, port))
        if result == 0:
            print('Port {}:      Ouvert'.format(port))
        sock.close()

except KeyboardInterrupt:
    print('Vous avez appuyé sur CTRL+C.')
    sys.exit()

except KeyboardInterrupt:
    print('Impossible de se connecter au serveur.')
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print('Scan complété en  : {}'.format(str(total)))
