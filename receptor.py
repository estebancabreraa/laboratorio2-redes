import socket
import pickle
import binascii
from bitarray import bitarray

class Receptor:
    
    def __init__(self, name):
        self.name = name
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.connect((socket.gethostname(), 1234))
        print("Se creo un receptor.")

    def enviar_cadena_segura(self, msg):
        cadena__binascii = bin(int.from_bytes(msg.encode(), 'big'))
        cadena__bitarray = bitarray(cadena__binascii[2:])
        self.enviar_objeto(cadena__bitarray)

    def enviar_cadena(self):
        self.enviar_cadena_segura("hola que tal")

    def recibir_objeto(self):
        data = self.sckt.recv(2048)
        cadena__bitarray = pickle.loads(data)
        print(cadena__bitarray)

re = Receptor("Raul")
re.recibir_objeto()
