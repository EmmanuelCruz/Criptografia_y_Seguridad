#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from utils import modinv

class Curve():

    def __init__(self, A, B, p):
        """
        Construcutor de clase que va a representar a la curva elíptica de la
        forma y^2 = x^3 + Ax + B (mod p).
        :param A: primer coeficiente de la curva.
        :param B: segundo coeficiente de la curva.
        :param p: el tamaño del campo sobre el cual se hace la curva.
        """
        self.A = A
        self.B = B
        self.p = p

    def is_on_curve(self, point):
        """
        Método de clase regresa true si un punto está en la curva, éste punto 
        está representado a manera de tupla, como (x, y).
        :param point: Una tupla de enteros representando a un punto.
        :return: true si el punto está en la curva, false en otro caso.
        """
        if point is None:
        	return True
        evaluado = ((point[0]**3) + (self.A*point[0]) + self.B) % self.p
        return pow(point[1], 2, self.p) == evaluado

    def determinant(self):
        """
        Regresa el determinante de una curva, recordando que su determinante
        es calculado de la forma 4A^3 + 27B^2.
        :return: El entero con el valor del determinante.
        """
        return 4*(self.A**3) + 27*(self.B**2)

def add_points(p, q, curve):
    """
    Dados un par de puntos y una curva elíptica, calcula el punto de la suma
    bajo la curva elíptica recibida como parámetro, se asume que p y q ya 
    forman parte de la curva.
    :param p: una tupla representando un punto de la curva.
    :param q: una tupla representando un punto de la curva.
    :param curve: una instancia de la clase de este script.
    :return: Una tupla que contiene el resultado de la suma o None en caso de
    que haya sido evaluada al punto infinito.
    """
    if p is None:
        return q
    if q is None:
        return p
    if p[0]==q[0] and p[1]!=q[1]:
        return None
    lambdaC = calculate_lambda(p, q, curve)
    x3 = (pow(lambdaC, 2) - p[0] - q[0]) % curve.p
    y3 = ((lambdaC * (p[0]-x3)) - p[1]) % curve.p
    return (x3, y3)

def calculate_lambda(p, q, curve):
	if p==q:
		return (3*pow(p[0],2) + curve.A) * modinv(2*p[1]%curve.p, curve.p)
	return (p[1]-q[1]) * modinv((p[0]-q[0])%curve.p, curve.p)

def scalar_multiplication(p, k, curve):
    """
    Dado un escalar del campo, k, calcula el punto kP bajo la definición
    de curvas elípticas.
    :param p: una tupla representando un punto de la curva.
    :param k: el escalar a multiplicar por el punto. 
    :param curve: la curva sobre la cual se calculan las operaciones.
    :return: una tupla representando a kP o None si al sumar ese punto cayó 
    en algún momento al punto infinito.
    """
    if k==1:
    	return p
    punto = scalar_multiplication(p, k-1, curve)
    return add_points(p, punto, curve)
