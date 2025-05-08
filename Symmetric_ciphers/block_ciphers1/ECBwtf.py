# ECB CBC WTF
from Crypto.Cipher import AES
from pwn import xor
import requests

def encrypt():
    url = "http://aes.cryptohack.org//ecbcbcwtf/encrypt_flag/"
    response = requests.get(url)
    return response.json()['ciphertext']

flag = encrypt()
f = [flag[i:i+32] for i in [0,32,64]]
vi = f[0:(len(f)-1)]
f = f[1:]
def decrypt(data):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    response = requests.get(url + data + '/')
    return response.json()['plaintext']

for i in range(len(f)):
    f[i] = decrypt(f[i])

for i in range(len(f)):
    f[i] = xor(bytes.fromhex(f[i]),bytes.fromhex(vi[i]))

flag = ""
for i in f:
    flag += i.decode()

print(flag)

##decrypts an AES-encrypted flag using a combination of ECB and CBC modes. 
# It first splits the encrypted flag into chunks and uses the initialization vector (IV)
# from the first chunk to decrypt the subsequent chunks. 
# Each chunk is XORed with its corresponding IV to convert from CBC mode to ECB mode. 
# The final decrypted flag is constructed by concatenating the plaintexts of all the chunks. 
# The script uses requests to interact with encryption and decryption endpoints and xor from pwn for the XOR operations