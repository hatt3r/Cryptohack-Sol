secret = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
tmp = bytes.fromhex(secret)
key = b'myXORkey'
[print(chr(key[i%len(key)]^v),end='') for i,v in enumerate(tmp)]


##Each character is XORed individually, 
# and the output is concatenated to form the decrypted string.