import socket
import pickle
import binascii
from bitarray import bitarray

def BitarrayToStr(array):
    result = ""
    for val in array:
        if val:
            result = result + "1"
        else:
            result = result + "0"
    return result

class Receptor:
    
    def __init__(self, name):
        self.name = name
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.connect((socket.gethostname(), 1234))
        print("Se creo un receptor.")

    def recibir_cadena(self, msg):
        print("Mensaje recibido: ", msg)

    def recibir_cadena_segura(self, cadena__bitarray):
        cadena__binascii = "0b" + BitarrayToStr(cadena__bitarray)
        msg_crudo = int(cadena__binascii, 2)
        msg = msg_crudo.to_bytes((msg_crudo.bit_length() + 7) // 8, 'big').decode()
        self.recibir_cadena(msg)

    def recibir_objeto(self):
        data = self.sckt.recv(2048)
        cadena__bitarray = pickle.loads(data)
        self.recibir_cadena_segura(cadena__bitarray)
        

re = Receptor("Raul")
re.recibir_objeto()
