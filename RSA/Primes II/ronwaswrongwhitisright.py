from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


msg = "???"

with open('21.pem') as f:
    key = RSA.importKey(f.read())

cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(msg)

with open('21.ciphertext', 'w') as f:
    f.write(ciphertext.hex())

## this opens the already extracted zip file 
# and chooses the 21.ciphertext to encrypt using the same number key
# so in this case 21.pem gives the encrypted output