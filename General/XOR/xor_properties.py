from pwn import *
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1xor2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2xor3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagxor123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key2 = xor(bytes.fromhex(key1xor2),key1)
key3 = xor(bytes.fromhex(key2xor3),key2)

key123 = xor(bytes.fromhex(key1xor2),key3)

flagbytes = xor(bytes.fromhex(flagxor123),key123)

print(str(flagbytes.decode()))

##calculates an intermediate key key2 by XORing key1xor2 with key1, 
# then finds key3 by XORing key2xor3 with key2. 
# These two keys (key2 and key3) are combined into key123. 
# The flagxor123 is then decrypted using key123 to get flagbytes,
# which is decoded into a string and printed.