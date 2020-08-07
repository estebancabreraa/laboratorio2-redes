from bitarray import bitarray

class FletcherChecksum:

    def generate_checksum(self, mes: bytes):
        size, fetch, a, b = 255, 8, 0, 0
        for b in mes:
            a = (a + b) % size
            b = (b + a) % size
        return str((b << fetch) | a)