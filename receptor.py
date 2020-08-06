import socket
import pickle
import binascii
from bitarray import bitarray
from fletcher import FletcherChecksum
from hamming import Hamming

def BitarrayToStr(array):
    result = ""
    for val in array:
        if val:
            result = result + "1"
        else:
            result = result + "0"
    return result

def write_log(log):
    with open("Hamming_con_ruido.csv", "a") as myfile:
        myfile.write(str(log) + "\n")

class Receptor:
    
    def __init__(self, name):
        self.name = name
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sckt.connect((socket.gethostname(), 1234))
        print("Se creo un receptor.")

    def recibir_cadena(self, msg):
        print("Mensaje recibido: ", msg)

    def recibir_cadena_segura(self, cadena__bitarray):
        cadena__binascii = "0b" + self.verificar(cadena__bitarray)
        msg_crudo = int(cadena__binascii, 2)
        msg = msg_crudo.to_bytes((msg_crudo.bit_length() + 7) // 8, 'big').decode()
        self.recibir_cadena(msg)

    def recibir_objeto(self):
        data = self.sckt.recv(2048)
        cadena__bitarray = pickle.loads(data)
        self.recibir_cadena_segura(cadena__bitarray)

    def convertir(self, message):
        result = ''
        for x in message:
            if (x):
                result = result + ''.join('1')
            else:
                result = result + ''.join('0')
        return result

    def verificar(self, message):
        bin_mes = self.convertir(message)
        hamming = Hamming()
        r = hamming.calcu_bit_red(len(bin_mes))
        error = hamming.detectar_error(bin_mes, r)
        print("El error se encuentra en la posicion ", error, " de la cadena binaria.")
        bin_mes = hamming.corregirMensaje(bin_mes, error)
        return bin_mes

    def decode(self, s, encoding='UTF-8'):
        byte_string = ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
        return byte_string.decode(encoding)

re = Receptor("Raul")
re.recibir_objeto()
