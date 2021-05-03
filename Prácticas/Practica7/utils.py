import math

def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def has_modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return False
    else:
        return True

def is_square(number):
    decimal, entero = math.modf(math.sqrt(number))
    return decimal == 0.0

def is_divisor(number, p):
    decimal, entero = math.modf(number/p)
    return decimal == 0.0