from math import sqrt, ceil
from random import randint
from ECM import lenstra

def sieve(n):
    arr = [True]*n
    root = ceil(sqrt(n))
    for i in xrange(2, int(root)):
        if arr[i]:
            j = i+i
            while j < n:
                arr[j] = False
                j += i
    primes = []
    for i in range(2, len(arr)):
        if(arr[i]):
            primes.append(i)
    return primes

def test_ecm():
    aux2 = lenstra(6)
    assert aux2 == (2, 3) or aux2 == (3, 2)
    aux1 = lenstra(130063)
    assert aux1 == (113, 1151) or aux1 == (1151, 113)
    criba = sieve(10000)
    p, q = criba[randint(0, len(criba))], criba[randint(0, len(criba))]
    aux = lenstra(p*q)
    assert aux == (p, q) or aux == (q, p)
