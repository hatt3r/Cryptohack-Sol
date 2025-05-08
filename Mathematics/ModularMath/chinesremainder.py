def chinese_remainder_theorem(moduli, remainders):
    def modinv(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    product = 1
    for m in moduli:
        product *= m

    result = 0
    for mi, ai in zip(moduli, remainders):
        bi = product // mi
        result += ai * modinv(bi, mi) * bi

    return result % product

moduli = [5, 11, 17]
remainders = [2, 3, 5]

result = chinese_remainder_theorem(moduli, remainders)
print("Flag: ", result)

##Chinese Remainder Theorem 
# to find a number that satisfies given moduli and remainders. 
# It calculates a result which is the number such that when divided by each modulus, 
# it leaves the corresponding remainder