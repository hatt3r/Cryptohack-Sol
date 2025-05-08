from Crypto.Util.number import long_to_bytes
n = 742449129124467073921545687640895127535705902454369756401331
e = 3 
ct = 39207274348578481322317340648475596807303160111338236677373
p =  752708788837165590355094155871
q =  986369682585281993933185289261
phi = (p-1)*(q-1)
d = pow(e,-1,phi) #decryption key 

decrypt = pow(ct,d,n)

print(long_to_bytes(decrypt))

## this is the decryption algo from the inferius.py 
# decrypts a ciphertext ct using the RSA private key d to retrieve the plaintext message. 
# It computes the decryption and then converts the resulting number back into bytes to reveal the original message.