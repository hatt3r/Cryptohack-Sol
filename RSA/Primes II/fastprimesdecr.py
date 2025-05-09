from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import long_to_bytes
from Crypto.Util import number
key = RSA.importKey(open("C:\\Users\\seren\\OneDrive\\Documents\\vscode\\Cryptohack\\RSA\\Primes II\\fastprimeskey.pem", "rb").read())
print("n= ",key.n)
print("e= ",key.e)
e=  65537
n = 4013610727845242593703438523892210066915884608065890652809524328518978287424865087812690502446831525755541263621651398962044653615723751218715649008058509
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161
phi = (p-1)*(q-1)
d = pow(e,-1,phi)
key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
hexc = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28
c = long_to_bytes(hexc)
m = cipher.decrypt(c)
print(m)

## reads an RSA key from the file mentioned, sets up the necessary parameters, 
# constructs a cipher using the PKCS1_OAEP scheme, 
# and then decrypts a hexadecimal ciphertext (hexc) to reveal the original message. 
# The decrypted message is printed.