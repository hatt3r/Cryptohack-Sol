from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) 
print(xor(flag, 'myXORkey'.encode())) 

##xor function to decrypt a hexadecimal-encoded flag.
# It first attempts to decode the flag by XORing it with the prefix 'crypto{', 
# and then tries to decode it with a different key 'myXORkey'. 
# Each XOR operation potentially decodes a different part of the flag