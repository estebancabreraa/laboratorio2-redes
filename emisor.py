import socket
import binascii
import bitarray

class Emisor:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(3)

    def __init__(self, name):
        self.name = name
        print("Se creo un emisor.")

    @staticmethod
    def enviar_cadena_segura(msg):
        cadena__binascii = bin(int.from_bytes(msg.encode(), 'big'))
        print (cadena__binascii)

    def enviar_cadena(self):
        self.enviar_cadena_segura("hola como estas")


em = Emisor("Esteban")
em.enviar_cadena()
