import sympy
import gmpy2


def mydecrypt(A, B):
    ans = 1
    temp = gmpy2.powmod(-1, 1, A)
    # print(temp)
    for i in range(B + 1, A):
        ans = (ans * gmpy2.invert(i, A)) % A
    return (ans * temp) % A


A1 = 
B1 = 
A2 = 
B2 = 
e = 
c = 
n = 
p = sympy.nextprime(mydecrypt(A1, B1))
q = sympy.nextprime(mydecrypt(A2, B2))
r = n // p // q
phi = (p - 1) * (q - 1) * (r - 1)
d = gmpy2.invert(e, phi)
flag = gmpy2.powmod(c, d, n)
import binascii

print(binascii.unhexlify(hex(flag)[2:]))
