import gmpy2
import binascii

e = 
n = 
d = 
c = 

m = gmpy2.powmod(c, d, n)
# print(m)
print(binascii.unhexlify(hex(m)[2:]))
