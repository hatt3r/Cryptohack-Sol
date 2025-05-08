import math
from decimal import *

getcontext().prec = 100

ciphertext = 1350995397927355657956786955603012410260017344805998076702828160316695004588429433

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

h = Decimal(ciphertext) / Decimal(16**64)

print(f"Initial h: {h}")

recovered_flag = ""
for i in range(len(PRIMES)):
    prime_sqrt = Decimal(PRIMES[i]).sqrt()
    
    print(f"Prime: {PRIMES[i]}, Sqrt: {prime_sqrt}")
    
    ord_c = int(h / prime_sqrt)
    
    print(f"Intermediate ord_c: {ord_c}, Character: {chr(ord_c)}")
    
    if ord_c < 32 or ord_c > 126:  
        ord_c = 32  
        print(f"Invalid ord_c, defaulting to space")
    
    recovered_flag += chr(ord_c)
    
    h -= ord_c * prime_sqrt
    print(f"Remaining h after character: {h}")

print(f"Recovered Flag: {recovered_flag}")

##Have cipher text and primes 
# decodes a large numeric ciphertext by iteratively deriving ASCII characters using square roots of prime numbers. 
# It starts by dividing the ciphertext by 1 6 64 16 64 to initialize a working value h. 
# For each prime in a predefined list, the script calculates the square root of the prime and divides 
# h by this square root to determine an ASCII value (ord_c). 
# If this value falls outside the printable ASCII range, it defaults to a space.
# The corresponding character is appended to the decoded flag, and 
# h is updated by subtracting the product of the ASCII value and the square root of the prime. 
