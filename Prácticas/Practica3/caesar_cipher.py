#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange

class Caesar():
	def __init__(self, alphabet, key=None):
        	self.alphabet=alphabet
	        self.cifrada=""
        	if key:
            		self.key=key
	        else:
        		self.key=randrange(len(alphabet))


	def decipher(self, criptotext, flag=None):
		resultado=""
		criptotext=criptotext.replace(" ","")
		for j in range(len(self.alphabet)):
			for i in range(len(criptotext)):
				if flag and criptotext[i]==" ":
					resultado+=" "
				else:
					if not criptotext[i]==" ":
						resultado+=self.alphabet[(self.alphabet.index(criptotext[i])-j)%len(self.alphabet)]
			print(j)
			print(resultado)
			resultado = ""
		return resultado

cesar = Caesar("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
cesar.decipher("PXUKANB VNLQXB ZDN JLDBJQB J TJ UDRNA BQV AJIXV BQV ENA ZDN BXQB TJ XLJBQXV MN TX UQBUX ZDN LDTYJQB BQ LXV JVBQJ BQV QODJT BXTQLQCJQB BD MNBMNV YXA ZDN ZDNANQB ZDN XKANV KQNV BQ TJB QVLQCJQB JT UJT")
