import threading
from receptor import Receptor
from emisor import Emisor

def iniciar_receptor(user):
    receptor = Receptor("user1")
    receptor.recibir_objeto()

def iniciar_emisor(user):
    emisor = Emisor(user)
    emisor.enviar_cadena()

if __name__ == "__main__":
    print('Se inicia el hilo para recpetor')
    rec = threading.Thread(target=iniciar_receptor)
    rec.start()

    print('Enviando mensaje')
    iniciar_emisor("user2")    
