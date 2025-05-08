message = 12
e = 65537
p = 17
q = 23

N = p * q

ciphertext = pow(message, e, N)
print(f"Ciphertext: {ciphertext}")

## we are given a message, e,p,q , then we find N and calculate ciphertext by power
# print the cipher text