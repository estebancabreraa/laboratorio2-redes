import socket
import binascii
from bitarray import bitarray

class Emisor:

    def __init__(self, name):
        self.name = name
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.bind((socket.gethostname(), 1234))
        self.sckt.listen(3)
        print("Se creo un emisor.")
    
    def enviar_objeto(self, cadena__bitarray):
        clientsocket, address = self.sckt.accept()
        clientsocket.send(cadena__bitarray)

    def enviar_cadena_segura(self, msg):
        cadena__binascii = bin(int.from_bytes(msg.encode(), 'big'))
        cadena__bitarray = bitarray(cadena__binascii[2:])
        self.enviar_objeto(cadena__bitarray)

    def enviar_cadena(self):
        self.enviar_cadena_segura("hola que tal")


em = Emisor("Esteban")
em.enviar_cadena()
