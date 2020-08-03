import socket
import pickle
import binascii
from random import randrange
from bitarray import bitarray

class Emisor:

    def __init__(self, name):
        self.name = name
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.bind((socket.gethostname(), 1234))
        self.sckt.listen(3)
        print("Se creo un emisor.")

    def cadena_con_ruido(self, cadena):
        caracter = randrange(0, 2)
        pos = randrange(0, len(cadena) - 1)
        cadena = cadena[:pos] + str(caracter) + cadena[pos+1:]
        return cadena
        
    
    def enviar_objeto(self, data):
        clientsocket, address = self.sckt.accept()
        clientsocket.send(data)

    def enviar_cadena_segura(self, msg):
        cadena__binascii = bin(int.from_bytes(msg.encode(), 'big'))
        cadena__bitarray = bitarray(self.cadena_con_ruido(cadena__binascii[2:]))
        data = pickle.dumps(cadena__bitarray)
        self.enviar_objeto(data)
        #self.enviar_objeto(cadena__binascii)

    def enviar_cadena(self):
        self.enviar_cadena_segura("hola que tal")


em = Emisor("Esteban")
em.enviar_cadena()

