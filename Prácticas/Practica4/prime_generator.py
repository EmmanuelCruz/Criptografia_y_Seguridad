#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

from random import randint
from random import randrange
import random
import datetime
import operator, functools

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    El algoritmo implementado es linear congruential generator
    Nos basamos de la pagina http://pi.math.cornell.edu/~mec/Winter2009/Luo/Linear%20Congruential%20Generator/linear%20congruential%20gen1.html
    para garantizar que no hace un ciclo y empieza a repetir digitos.
    Esto sucede asi porque m y c son primos relativos y a-1 divide a todos los factores primos de m
    """
    if (size is None) or (size < 100):
        size = randint(100,150)
    date_object = datetime.date.today()
    time = datetime.datetime.now()
    numero = ""
    x = 2
    m = 1299827
    a = 2
    c = int(date_object.year) + int(date_object.month) + int(date_object.month) + int(date_object.day) + int(time.hour) + int(time.minute) + int(time.second)
    i = 0
    while(i < size and len(numero) < size):
        x = (a*x + c)%m
        numero += str(x)
        i += 1
    return int(numero[0:size])

def power(x, y, p): 
      
    # Initialize result 
    res = 1;  
      
    # Update x if it is more than or 
    # equal to p 
    x = x % p;  
    while (y > 0): 
          
        # If y is odd, multiply 
        # x with result 
        if (y & 1): 
            res = (res * x) % p; 
  
        # y must be even now 
        y = y>>1; # y = y/2 
        x = (x * x) % p; 
      
    return res; 
    
def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    if n==2 or n==3:
        return True
    d = discompose(n)

    #Si d = -1, n era un número par no primo
    if (d == -1): return False 
    
    a = randint(2,n-2)

    #Saco la congruencia mayor de potencias menores para evitar manejar números grandes.
    x = power(a,d,n)

    #Este if es verifica que la condición de Fermat para el caso "base"
    #Encontrar una explicacion matemática mejor...sí es necesario para los test
    if (x == 1 or x == n - 1): 
       return True; 
       
    #aumento las potencias de 2 por la cuales se multiplica a d hasta llegar a n-1
    #lo cual va a suceder porque 2**s * d = n-1
    while d < n-1:
        #aumento la potencia de a en una unidad (a**d * a**d) % n
        x = (x*x) % n
        
        #ídem con potencia de 2
        d = d*2
        
        # a**((2**j)* d) % n == n-1, encontré un j para el cual vale
        # luego es primo (x no deja de ser x = a * a * a * a ...así d+1 veces tras línea 78)
        if (x % n == n - 1): 
            return True; 
        
        #este if no sé bien qué hace, no es necesario para que los tests den OK.
        #lo borramos? nos preguntará?
        if (x % n == 1): 
            return False; 
   
    return False

#Observación: para chequear el Test de Miller-Rabin no es necesario el factor r.
#Luego, por eso no se calcula
def discompose(n):
    """
    Función auxiliar que permite hallar el parámetro d de la siguiente descomposición
    de un número n, con n !=2
    n = ((2**r)*d)+1
    :param n: El número a descomponer.
    :return d: El elemento r de la descomposición o -1 si es par
    """
    #Si es par, luego sabemos que no es primo
    if(n % 2 == 0):
        return -1
        
    #Reduzco las potencias de 2 hasta hallar a d, el cual es par
    d = n - 1
    while (d % 2 == 0):
        d = d//2
    return d*2

def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    numbers = list(range(n))
    fact = functools.reduce(operator.mul, numbers[2:len(numbers)], 1)
    return fact%n == -1%n


