#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils import prime_relative
from utils import find_prime_relative
from utils import mcd_and_quoef
from random import randrange

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        self.alphabet=alphabet
        self.cifrada=""
        if A:
            self.A=A
        else:
            self.A=find_prime_relative(len(alphabet))
        if B:
            self.B=B
        else:
            self.B=randrange(len(alphabet))


    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        resultado=""
        for i in range(len(message)):
            resultado+=self.alphabet[(self.alphabet.index(message[i].upper())*self.A+self.B)%len(self.alphabet)]
        self.cifrada=resultado
        return self.cifrada

    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        resultado=""
        mcd, u, v = mcd_and_quoef(len(self.alphabet), self.A);
        if mcd == 1:
            v = v%len(self.alphabet)
            des = []
            for i in range(len(criptotext)):
                resultado+=self.alphabet[v*(self.alphabet.index(criptotext[i])-self.B)%len(self.alphabet)]
            return resultado

