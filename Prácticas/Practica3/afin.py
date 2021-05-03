#!/usr/bin/python
# -*- coding: utf-8 -*-
f=open("Cifrados/Three.txt","r")
dato=f.read()
nuevo=open("fuera.txt","w")
alphabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cadena = ""
final = ""
for n in range(27):
	for j in range(27):
		for i in range(len(dato)):
			aux = 0
			aux += alphabeto.find(dato[i])-n
			cadena += alphabeto[(aux*j)%27]
		print(cadena)
		print(n,j)
		cadena = ""
nuevo.close()
f.close()
