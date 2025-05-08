from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
import random

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = Cipher(algorithms.AES(password_hash), modes.ECB())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted = unpadder.update(decrypted) + unpadder.finalize()
    return decrypted

with open("\words.txt") as f:
    words = [w.strip() for w in f.readlines()]
    
keyword = random.choice(words)

def generate_key(word):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(word.encode())
    return digest.finalize()

l = len(words)

for i in range(l):
    key = generate_key(words[i])
    decrypted = decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", key)
    if b'crypto' in decrypted:
        print(decrypted.decode('utf-8', errors='ignore'))
        break

## attempts to decrypt a ciphertext using AES with a randomly selected key
# from list of words from the file words.txt striping it then checkiing
# if the decrypted key contains the word 'crypto' then print it by decoding with utf-8