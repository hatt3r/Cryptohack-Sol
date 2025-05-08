from Crypto.Util.number import *

flag = b"ZeroDays{REDACTED}"
m = bytes_to_long(flag)
e = 65537

# This takes way too long!
p = getPrime(512)

# Let's just speed it up
i = 2
while True:
    if isPrime(p+i):
        q = p+i
        break
    i += 2

n = p*q
c = pow(m,e,n)

print(f"{n = }")
print(f"{c = }")
