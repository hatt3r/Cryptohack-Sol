secret = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
tmp = bytes.fromhex(secret)
for i,v in enumerate('crypto{'):
    print(chr(tmp[i]^ord(v)),end='')

##applies XOR decryption on each byte based on its position 
# in the hex string relative to the characters in 'crypto{'