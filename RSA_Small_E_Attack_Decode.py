# python3
# -*- coding: utf-8 -*-#

from gmpy2 import iroot
import libnum

e = 
n = 
c = 

k = 0
while 1:
    res = iroot(c + k * n, e)  # c+k*n 开3次方根 能开3次方即可
    # print(res)
    if (res[1] == True):
        print(libnum.n2s(int(res[0])))  # 转为字符串
        break
    k = k + 1
