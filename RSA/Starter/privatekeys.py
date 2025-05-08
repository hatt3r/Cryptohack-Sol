from sympy import mod_inverse


p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537


N = p * q
phi_N = (p - 1) * (q - 1)


d = mod_inverse(e, phi_N)

print(f"Private key d: {d}")

## we are given p q and e values we calculate N = p*q and phi 
# with this we use mod_inverse function from sympy module to calculate private key
