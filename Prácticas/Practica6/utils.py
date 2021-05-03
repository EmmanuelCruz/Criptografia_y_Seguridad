def prime_relative(a, b):
    if(b == 0):
    	return a == 1
    else:
        return prime_relative(b, a%b)

def mcd_and_quoef(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	mcd = b
	return y

def mcd(a, b):
	if b == 0:
		return a
	return mcd(b, a%b)