#!/usr/bin/env python3

import random
from Crypto.Util.number import bytes_to_long, isPrime

FLAG = b"crypto{???????????????????}"


def getPrimes(bitsize):
    r = random.getrandbits(bitsize)
    p, q = r, r
    while not isPrime(p):
        p += random.getrandbits(bitsize//4)
    while not isPrime(q):
        q += random.getrandbits(bitsize//8)
    return p, q


m = bytes_to_long(FLAG)
p, q = getPrimes(2048)
n = p * q
e = 0x10001
c = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")

## this file came with the challenged but what it does is 
# generates a pair of prime numbers p and q with a bit size of 2048, calculates the modulus n, 
# and encrypts a given message (represented as FLAG) using RSA encryption with an exponent e of 0x10001. 
# The results (modulus n, exponent e, and ciphertext c) are printed.