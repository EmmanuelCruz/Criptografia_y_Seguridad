#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import EllipticCurves as ec
from random import randint
from utils import is_square, modinv
import math

class ECIES():

    def __init__(self, curve, A, B, N, s, p):
        self.curve = curve
        self.A = A
        self.B = B
        self.N = N
        self.s = s
        self.p = p
        self.alphabet = "ABCDEFGHIJKLMN\xc3OPQRSTUVWXYZ"

    def encrypt(self, message):
    	lista = list()
    	k = randint(1, self.N-1)
        for c in message:
        	U = ec.scalar_multiplication(self.A, k, self.curve)
        	V = ec.scalar_multiplication(self.B, k, self.curve)
        	p_compresion = (U[0], U[1] % 2)
        	x = (self.alphabet.find(c)*V[0]) % self.curve.p
        	lista.append((p_compresion, x))
        return lista

    def decrypt(self, criptotext):
    	message = ""
    	for c in criptotext:
    		punto, x = c
    		s = (pow(punto[0], 3) + self.curve.A*punto[0] + self.curve.B) % self.curve.p
    		while not is_square(s):
    			s += self.curve.p
    		raiz = int(math.sqrt(s))
    		if punto[1]==1:
    			raiz *= -1
    		pt_desc = ec.scalar_multiplication((punto[0], raiz), self.s, self.curve)
    		valorFinal = (x * modinv(pt_desc[0]%self.curve.p, self.curve.p)) % self.p
    		message += self.alphabet[valorFinal]
        return message
