import socket
import pickle
import binascii
from random import randrange
from bitarray import bitarray
from fletcher import FletcherChecksum
from hamming import Hamming

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

    def convertir(self, message):
        result = ''
        for x in message:
            result = result + ''.join(format(ord(x),'b')) 
        return result
    
    def verificar(self, message):
        bin_mes = self.convertir(message)
        hamming = Hamming()
        r = hamming.calcu_bit_red(len(bin_mes))
        bin_mes = hamming.pos_bit_red(bin_mes, r)
        bin_mes = hamming.calcu_bit_par(bin_mes, r)
        message = bitarray(bin_mes)
        return message

    


em = Emisor("Esteban")
em.enviar_cadena()

