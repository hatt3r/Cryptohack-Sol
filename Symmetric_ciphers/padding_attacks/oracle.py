from pwn import*
from Crypto.Util.number import*

io = remote("localhost", 1337)

io.sendline(b'encrypt')
encrypt = io.recvuntil(b'\n')
encrypt = encrypt[:-1].decode()
encrypt = bytes.fromhex(encrypt)
iv = encrypt[:16]
ciphertext = encrypt[16:]
ciphertext1 = ciphertext[:16]
ciphertext2 = ciphertext[16:32]
print(ciphertext1.hex())
print(ciphertext2.hex())

plaintext2 = b''
new_xor = b""
for i in range(1,17):
    temp = ciphertext1[:16-i]
    for b in range(256):
        if len(plaintext2) > 0:
            pad = long_to_bytes(i)*(i-1)
            send = temp + long_to_bytes(b) + xor(pad, new_xor) + ciphertext[16:]
        else:
            send = temp + long_to_bytes(b) + ciphertext[16:]

        io.sendline(b'decrypt')
        io.recvuntil(b'Ciphertext: ')
        io.sendline(send.hex().encode())
        receive = io.recvuntil(b'\n',drop=True)

        receive = io.recvuntil(b'\n',drop=True).decode()

        receive = io.recvuntil(b'\n',drop=True)
        if receive == b'Decrypted successfully.':

            new_xor = xor(long_to_bytes(i),(b)) + new_xor
            plaintext2 = xor(xor(long_to_bytes(i),(b)), (ciphertext[16-i:17-i])) + plaintext2
            print(plaintext2)
            break
        
        
## my attempt at oracle was unsuccessfull