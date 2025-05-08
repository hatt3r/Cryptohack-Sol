from sympy import factorint

N = 510143758735509025530880200653196460532653147

factors = factorint(N)

smaller_prime = min(factors)
print(f"Smaller prime factor: {smaller_prime}")

## factorize a large integer N and then finds and prints the smallest prime factor.