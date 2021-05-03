#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange

class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parametro todos los atributos
        que necesita el algoritmo de cifrado de Cesar.
        Parametro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamano del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, valida.
        """
        self.alphabet=alphabet
        self.cifrada=""
        if key:
            self.key=key
        else:
            self.key=randrange(len(alphabet))

    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parametro con el algoritmo de
        cifrado cesar, un desplazamiento sobre el alfabeto predefinido.
        Parametro:
            message -- el mensaje a cifrar.
        """
        resultado=""
        if self.alphabet.find(" ")>0:
        	for j in range(len(message)):
        		resultado+=self.alphabet[(self.alphabet.index(message[j].upper())+self.key)%len(self.alphabet)]
        else:
        	for i in range(len(message)):
        		if flag and message[i]==" ":
        			resultado+=" "
        		else:
        			if not message[i]==" ":
        				resultado+=self.alphabet[(self.alphabet.index(message[i].upper())+self.key)%len(self.alphabet)]
        self.cifrada=resultado
        return self.cifrada

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de cesar.
        Parametro:
            cryptotext -- el mensaje a descifrar.
        """
        resultado=""
        for i in range(len(criptotext)):
        	if flag and criptotext[i]==" ":
        		resultado+=" "
        	else:
        		if not criptotext[i]==" ":
        			resultado+=self.alphabet[(self.alphabet.index(criptotext[i])-self.key)%len(self.alphabet)]
        return resultado