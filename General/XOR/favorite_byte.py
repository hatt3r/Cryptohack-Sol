from pwn import *
giv = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
giv = bytes.fromhex(giv)
for i in range(0,99):
    print(xor(giv,i))

##converts a hexadecimal string to bytes and performs an XOR operation 
# with a range of integers (from 0 to 98) as keys. 
# It prints the result of each XOR operation.