from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))

## converts each byte of the flag into a binary string and randomly selects an exponent e. 
# For each bit, it calculates a^e % p. 
# If the bit is 1, the result is added to the ciphertext; 
# if the bit is 0, the negative of the result is added. 
