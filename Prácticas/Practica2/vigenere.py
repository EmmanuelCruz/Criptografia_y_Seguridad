#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random as rn
import math as mt

class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tama\xc3o del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tama\xc3o 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet=alphabet
        if password:
        	self.password=password
        else:
            self.password=""
            length=rn.randint(6,rn.randint(7,100))
            for i in range(length):
                self.password+=self.alphabet[rn.randint(0,len(self.alphabet)-1)]

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        result=""
        for i in range(len(message)):
        	result+=self.alphabet[(self.alphabet.index(message[i])+
        							self.alphabet.index(self.password[i%len(self.password)]))%
        							len(self.alphabet)]
        return result

    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        result=""
        for i in range(len(ciphered)):
        	result+=self.alphabet[(self.alphabet.index(ciphered[i])-
        							self.alphabet.index(self.password[i%len(self.password)]))%
        							len(self.alphabet)]
        return result
