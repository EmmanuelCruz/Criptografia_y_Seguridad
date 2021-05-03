#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import EllipticCurves as ec
from random import randint
from utils import prime_relative, is_divisor, has_modinv
from fractions import gcd

def lenstra(n):
    """
    Implementación del algoritmo de Lenstra para encontrar los factores
    primos de un número n de la forma n = p*q. Se asume que la proposición
    anterior es cierta, es decir, que en efecto n = p*q, regresando ambos
    factores de n.
    """
    a, x, y = randint(1,n-1), randint(1,n-1), randint(1,n-1)
    b = (pow(y,2) - pow(x,3) - (a * x)) % n
    E = ec.Curve(a, b, n)
    while not prime_relative(E.determinant(), n):
    	a, x, y = randint(1,n-1), randint(1,n-1), randint(1,n-1)
    	b = (pow(y,2) - pow(x,3) - (a * x)) % n
    	E = ec.Curve(a, b, n)
    p = (x, y)
    while not E.is_on_curve(p):
    	p = (randint(1,n), randint(1,n))
    lamb = calculate_lambda(p, p)
    point_aux = p
    while has_modinv(lamb, n):
    	point_aux = ec.add_points(p, point_aux, E)
    	lamb = calculate_lambda(p, point_aux)
    p = gcd(lamb, n)
    q = n/p
    if p==1 or q==1:
    	return lenstra(n)
    return (p, q)

def calculate_lambda(p, q):
	if p==q:
		return 2*p[1]
	return p[0]-q[0]
