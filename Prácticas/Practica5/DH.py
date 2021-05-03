#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

from random import randint

class Participant():


    def __init__(self, p, g, participant):
        """
        Constructor de clase
        """
        self.p = p
        self.g = g % p
        self.participant = participant
        self.k = randint(0,p)

    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        return (g**self.k) % p

    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """
        return (self.participant.seed()**self.k) % p


p, g = 103, 78
A, B = Participant(p, g, None), Participant(p, g, None)
A.participant = B
B.participant = A
keyA = A.exchange()
keyB = B.exchange()

print(keyA)
print(keyB)