#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

from prime_generator import generate_prime, miller_rabin
from utils import prime_relative, mcd, mcd_and_quoef
from random import randint
from random import randrange
import math

class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        #Aquí también deben de generar su priv_key y pub_key
        self.p = generate_prime(100)
        self.q = generate_prime(100)
        #p = 37
        #q = 61
        self.n = self.p*self.q
        phiN = self.__phi__()
        e = randint(1, phiN)
        d = mcd_and_quoef(phiN, e)
        while not prime_relative(e,phiN) or d<0:
        	e = randint(1, phiN)
        	d = mcd_and_quoef(phiN, e)
        self.pub_key = e
        self.priv_key = d
        pub_keyFile = open("pub_key.pem",'w')
        priv_keyFile = open("priv_key.pem",'w')
        pub_keyFile.write(str(self.n)+"\n")
        pub_keyFile.write(str(self.pub_key))
        pub_keyFile.close()
        priv_keyFile.write(str(self.n)+"\n")
        priv_keyFile.write(str(self.priv_key))
        priv_keyFile.close()
        self.b = 9
        self.padding_scheme = True

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        
        return (self.p-1)*(self.q-1)

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        cifrado = list()
        while len(message)%3 != 0:
        	message += " "
        i = 0
        bloque = self.b/3
        while i < len(message)-2:
        	num1 = str(ord(message[i]))
        	num2 = str(ord(message[i+1]))
        	num3 = str(ord(message[i+2]))
        	while len(num2)<bloque:
        		num2 = "0"+num2
        	while len(num3)<bloque:
        		num3 = "0"+num3
        	compuesto = int(num1+num2+num3)
        	numero = pow(compuesto, self.pub_key, self.n)
        	cifrado.append(numero)
        	i+=3
        """
        for m in message:
        	numero = pow(ord(m), self.pub_key, self.n)
        	cifrado.append(numero)
        """
        return cifrado

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        message = ""
        bloque = self.b//3
        for c in criptotext:
        	numero = pow(c, self.priv_key, self.n)
        	representacion = str(numero)
        	while len(representacion) < self.b:
        		representacion = "0"+representacion
        	caracter1 = representacion[:bloque]
        	caracter2 = representacion[bloque:bloque*2]
        	caracter3 = representacion[bloque*2:]
        	message += chr(int(caracter1)%256) + chr(int(caracter2)%256) + chr(int(caracter3)%256)
        """
        for c in criptotext:
        	numero = pow(c, self.priv_key, self.n)
        	message += chr(numero%256)
        """
        return message.strip()

