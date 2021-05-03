class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)

def find_prime_relative(longitud):
	iterador=12
	while prime_relative(longitud, iterador)!=1:
		iterador+=1
	return iterador

def mcd_and_quoef(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	mcd = b
	return mcd, x, y

print(find_prime_relative(256))
