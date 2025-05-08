from Crypto.Util.number import *

flag = b"ZeroDays{REDACTED}"
m = bytes_to_long(flag)
e = 65537

# This time I'll do it a little differently
while True:
    p = getPrime(512)
    q = (2*p)-1
    if isPrime(q):
        break

n = p*q
c = pow(m,e,n)

print(f"{n = }")
print(f"{c = }")
