from Crypto.Util.number import *
import gmpy2

n = 
e1 = 
e2 = 
c1 = 
c2 = 


# 共模解密
def Rsa_Gong_N_Attack(n, e1, e2, c1, c2):
    n, e1, e2, c1, c2 = int(n), int(e1), int(e2), int(c1), int(c2)
    s = gmpy2.gcdext(e1, e2)
    s1 = s[1]
    s2 = s[2]
    # 求模反元素
    if s1 < 0:
        s1 = -s1
        c1 = gmpy2.invert(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = gmpy2.invert(c2, n)
    m = (pow(c1, s1, n) * pow(c2, s2, n)) % n
    return int(m)


m = Rsa_Gong_N_Attack(n, e1, e2, c1, c2)
print(m)
print(long_to_bytes(m))
