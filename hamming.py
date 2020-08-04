from bitarray import bitarray

class Hamming:

    def calcu_bit_red(self, n):   
        for i in range(n): 
            if(2**i >= n + i + 1): 
                return i 

    def pos_bit_red(self, data, r): 
        j, k = 0, 1
        m = len(data)
        result = '' 

        for i in range(1, m + r+1): 
            if(i == 2**j): 
                result = result + '0'
                j += 1
            else: 
                result = result + data[-1 * k] 
                k += 1
        return result[::-1] 

    def calcu_bit_par(self, data, r): 
        n = len(data) 
        for i in range(r): 
            value = 0
            for j in range(1, n + 1):  
                if(j & (2**i) == (2**i)): 
                    value = value ^ int(data[-1 * j]) 
            data = data[:n-(2**i)] + str(value) + data[n-(2**i)+1:] 
        return data

    def detectar_error(self, data, r): 
        n = len(data) 
        result = 0
        for i in range(r): 
            value = 0
            for j in range(1, n + 1): 
                if(j & (2**i) == (2**i)): 
                    value = value ^ int(data[-1 * j])     
            result = result + value*(10**i) 
        return int(str(result), 2) 

    def corregirMensaje(self, bin_mes, error):
        if(error > len(bin_mes)):
            return bin_mes
        error = error - 1
        bin_mes = list(bin_mes)
        if (bin_mes[error] == '0'):
            bin_mes[error] = '1'
        else:
            bin_mes[error] = '0'
        return ''.join(bin_mes)

    
                    
 