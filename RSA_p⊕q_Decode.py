# written by : 21r000
# !/usr/bin/env python3

import math
import gmpy2
import binascii


def check_cong(k, _p, _q, _n, xored=None):
    kmask = (1 << k) - 1
    _p &= kmask
    _q &= kmask
    _n &= kmask
    pqm = (_p * _q) & kmask
    return pqm == _n and (xored is None or (_p ^ _q) == (xored & kmask))


def extend(k, a):
    kbit = 1 << (k - 1)
    assert a < kbit
    yield a
    yield a | kbit


def factor(_n, p_xor_q):
    tracked = set([(_p, _q) for _p in [0, 1] for _q in [0, 1]
                   if check_cong(1, _p, _q, _n, p_xor_q)])

    PRIME_BITS = int(math.ceil(math.log(_n, 2) / 2))

    maxtracked = len(tracked)
    for k in range(2, PRIME_BITS + 1):
        newset = set()
        for tp, tq in tracked:
            for newp_ in extend(k, tp):
                for newq_ in extend(k, tq):
                    # Remove symmetry
                    newp, newq = sorted([newp_, newq_])
                    if check_cong(k, newp, newq, _n, p_xor_q):
                        newset.add((newp, newq))

        tracked = newset
        if len(tracked) > maxtracked:
            maxtracked = len(tracked)
    print('Tracked set size: {} (max={})'.format(len(tracked), maxtracked))

    # go through the tracked set and pick the correct (p, q)
    for _p, _q in tracked:
        if _p != 1 and _p * _q == _n:
            return _p, _q

    assert False, 'factors were not in tracked set. Is your p^q correct?'


e = 
n = 
c = 
p_q = 

p, q = factor(n, p_q)
print("p =", p)
print("q =", q)

d = gmpy2.invert(e, (p - 1) * (q - 1))
m = gmpy2.powmod(c, d, n)

print(binascii.unhexlify(hex(m)[2:]))
