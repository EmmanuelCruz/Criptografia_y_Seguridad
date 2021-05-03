import random
import math
import numpy as np
import sympy as sym
from utils import CryptographyException

class Hill():

    def __init__(self, alphabet, n, key=None):
        self.alphabet = alphabet
        self.n = n
        decimal, entera = math.modf(math.sqrt(self.n))
        if key and decimal==0:
            self.key = self.generate_key(key)
            if(len(self.alphabet)%int(np.linalg.det(self.key)) == 0):
                raise CryptographyException()
        else:
            self.key = self.generate_key()
            
    def cipher(self, message):
        message = message.replace(" ","")
        ciphermessage = ""
        raiz = int(math.sqrt(self.n))
        i=0
        while i<len(message):
            a = []
            for j in range(raiz):
                if i<len(message):
                    a.append(self.alphabet.index(message[i]))
                else:
                    a.append(0)
                i+=1
            matriz=np.array(a).reshape(raiz,1)
            mult = np.dot(self.key, a)
            ciphermessage += self.cipher_sqrt_chars(mult)
        return ciphermessage

    def cipher_sqrt_chars(self,matriz):
        resultado = ""
        raiz = int(math.sqrt(self.n))
        for i in range(raiz):
            resultado += self.alphabet[int(matriz[i]%len(self.alphabet))]
        return resultado

    def modInverse(self, a, m): 
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1

    def decipher(self, message):
        message = message.replace(" ","")
        raiz=int(math.sqrt(self.n))
        ciphermessage = ""
        matriz = sym.Matrix(self.key.tolist())
        inversa = self.modInverse(math.ceil(np.linalg.det(self.key)),len(self.alphabet))
        mult = (inversa * matriz.adjugate() % len(self.alphabet))
        i = 0
        while i<len(message):
            a = []
            for j in range(raiz):
                a.append(self.alphabet.index(message[i]))
                i+=1
            a = ( mult * sym.Matrix(a) ) % len(self.alphabet)
            ciphermessage += ''.join([self.alphabet[x] for x in a])
        return ciphermessage

    def generate_key(self, key=None):
        raiz=int(math.sqrt(self.n))
        b = []
        llave=""
        if key:
            llave=key
        else:
            for i in range(self.n):
                llave += self.alphabet[random.randint(0,len(self.alphabet)-1)]
        
        for j in range(self.n):
            b.append(self.alphabet.index(llave[j]))
        
        matriz=np.array(b).reshape(raiz,raiz)
        determinante=np.linalg.det(matriz)
        while( round(determinante) == 0 or self.mcd(round((np.linalg.det(matriz))) % 27, 27) != 1):
            llave=""
            b = []
            for k in range(self.n):
                llave += self.alphabet[random.randint(0,len(self.alphabet)-1)]
            
            for j in range(self.n):
                b.append(self.alphabet.index(llave[j]))
        
            matriz=np.array(b).reshape(raiz,raiz)
            determinante=np.linalg.det(matriz)
        return matriz
    
    def mcd(self,a, b):
      resto = 0
      while(b > 0):
        resto = b
        b = a % b
        a = resto
      return a
    
def test_random_key():
    cipher = Hill(alphabet, 4)
    c1 = cipher.cipher("UN MENSAJE CON \xc3")
    assert cipher.decipher(c1) == "UNMENSAJECON\xc3A"
    c2 = cipher.cipher("UN MENSAJE DE LONGITUD PAR")
    assert cipher.decipher(c2) == "UNMENSAJEDELONGITUDPAR"
