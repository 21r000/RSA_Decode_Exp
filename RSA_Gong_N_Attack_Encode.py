from Crypto.Util.number import *

flag = b''

p = getPrime(1024)
q = getPrime(1024)
e1 = 
e2 = 
m = bytes_to_long(flag)
n = p * q
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
print("n = ", n)
print("e1 = ", e1)
print("e2 = ", e2)
print("c1 = ", c1)
print("c2 = ", c2)
