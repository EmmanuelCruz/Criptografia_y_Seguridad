#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#import os, sys
import random
import math
import numpy as np
import sympy as sym
from utils import CryptographyException

class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamaÑHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaÑo de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
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
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
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
        """
        Funcion auxiliar que hace el cifrado de dos caracteres,utilizando
        el cifrado hill.
        :param indice: el indice desde el cual empezamos a tomar los caracteres
        del mensaje que se recibe como parametro.
        :param message: el mensaje que queremos cifrar
        :return: un string con los dos caracteres cifrados.
        """
        resultado = ""
        raiz = int(math.sqrt(self.n))
        for i in range(raiz):
            resultado += self.alphabet[int(matriz[i]%len(self.alphabet))]
        return resultado

    def modInverse(self, a, m): 
        """Funcion para calcular el
        inverso de un numero a modulo m, tomado de
        geeks for geeks
        """
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1

    def decipher(self, message):
        message = message.replace(" ","")
        raiz=int(math.sqrt(self.n))
        ciphermessage = ""
        matriz = sym.Matrix([[5,25],[7,2]])
        inversa = self.modInverse(-165,len(self.alphabet))
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
    c1 = cipher.cipher("UN MENSAJE CON Ñ")
    assert cipher.decipher(c1) == "UNMENSAJECONÑA"
    c2 = cipher.cipher("UN MENSAJE DE LONGITUD PAR")
    assert cipher.decipher(c2) == "UNMENSAJEDELONGITUDPAR"


hill = Hill("ABCDEFGHIJKLMNOPQRSTUVWXYZ",4,"FZHC")
print(hill.decipher("DZBNJDNLEMMWDFAWKOJYWQLRFGDFLDDZDFUIHCDZLLIGIWPMSSHPYEFGRDBXJDWLAECEHCJTRZWQJCCMLDAWLJMSKAKMUZAEJXTIOYDAZPXZCEHCDFUGTEIKOCCJIKLKUCJCPMDAAENEAENYKMQSJCJYEMTMXKYEFXDKFUZHUOZIJDLDAWZHDFYWTQWOCEDPPBLDUITWVQPAUCCNDKKGOAHCCMBCIQBEJIFUDZRZPBYYRZAADFAWKOBEALPAUOKMKTHQNAQYAGKTAQLRFUTIVQYGHCNLLGJTUILDDZIGNLZFKGSSLDZPAWNNTRNNDFUICMLDCEZFKTTUWONGZHHCDZZHHZWKNYKMEQLDUITWVQQYDXOEIWPBMWDFUIIEHPTBFDLLVNCMYYVPBXJCFSAEBEWQTKDXEMUDCMMSKTCMALUOJTUDCMASSSIEUITHNAHCTBEOTRBERZFDDFJDDXZHXAYEAGBRCEAEOOJKSKEMLDIKDZJCJODKHCCEIKLDLLVNCWRDIGZPLDPBMWDFUIJCBODKAWNNFHCJIKGJDYKMPVLDJCJYOYHMDKOECMRDIEXASGLGYEAGJVHGSSTRCJSSQSWQUZBEWKPVXABCFGMIFSPACMOYAEEMXXHCDZNLBCOEHMGSMIUMZFOOWIUGIQFDRZKOJTBRLDODJKDFLDTHTITOWODFZFWQLWDAAENEMIQYJISGRIZSPWBCCEHCJTRZWQDPCMZPIEFXKTWIZPNRDKBRCEFUCMLDDZNNXRHPZHVTFDHCEOHLCEFUCMGJSSFHOSXWTJZFEOUZAEXBHPPBGIZFOOAEDZCEHCCEYEFUTIVQOAHMNAYYPBJKIKTJRAPACMEUWONLIGRZPBYYRZWQEOHLNANLJYQCPWLVKAZCNAJKHMGEZFUMHCDKPWIWQKWJVPKOHPJYJKTUDKYYWQJVTIPMBEJYPBSKMWFHLRIKKMJJJNEMBREOUZJYOYHMIAHMMICWJYHPHVNNAWHCDFQCNABXJXUDNALDDZRZEMKOFXUCEMIWFGDZDFPJJIWODFNLZHMWRDKOTRCJHMGEZFAADFAWKOYYOPTEIKCMRZPBYYRZKOOSZPCEHCJTRZKOIEJVVRRAGSKMUZHPXGIAQYZFDFTWMSKGSSDZIGNLZFNAAEFGPAOEUIXZDXJVZHXAYEAGEMJVIPYEAGASSSDZJNTXFUEMTIOELDMHLELKGSXKCCKMUZPAFGJIJTQCDZMWALFQCMLDIPIKAGMXHMFUDXDCBYZCPWSQLDKGSSHMZFLVDFKAGSRWFUPVBXBPSVVAVKSSHPVXCCMXIAHCNLIGFDVRTIYEAGJVAUSGNAMIIKLDHMGSAEIGNLZFPWCMLDRXWOUIUIBXJIWODFNLZHZWSUGWENZCPWWIDVTIHCCEXGJYBRCEDYSSZWDYPAOEWQLRTEXMIWJYAEQCDKJDKACWDKNAWQFDKEPWHPPRLDRBTBSDYEAGJYDPUZPAZSWORDJIWODFNLVPWQGJZSPWSGAGHCDZAQTRXBEOHLZSPWFIYEKMLROELDPBTIGEPBQSKAZFTIOEZPUGTEIKOCCJJIZSJYYEAGPJDZHPHVBLZGTUDYBCJYQCPWDZEMLDIKLDLDUITWVQNESSTRWVFGTQOEPVXABCWQVXLKDKJIIEDZAUHMDKOEVPTIIKQMNLIK"))
