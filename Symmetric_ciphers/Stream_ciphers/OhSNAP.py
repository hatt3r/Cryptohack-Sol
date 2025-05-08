from Crypto.Cipher import ARC4 
import requests 
import json 

def swapValueByIndex(box, i, j):
    temp = box[i]
    box[i] = box[j]
    box[j] = temp

def initSBox(box):
    if len(box) == 0:
        for i in range(256):
            box.append(i)
    else:
        for i in range(256):
            box[i] = i

def ksa(key, box):
    j = 0
    for i in range(256):
        j = (j + box[i] + key[i % len(key)]) % 256
        swapValueByIndex(box, i, j)

def prga(plain, box, keyStream, output):
    i = 0
    j = 0
    for i in range(len(plain)):
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        swapValueByIndex(box, i, j)
        keyStreamByte = box[(box[i] + box[j]) % 256]
        outputByte = plain[i - 1] ^ keyStreamByte
        keyStream += bytes([keyStreamByte])
        output += bytes([outputByte])
    return (keyStream, output)

box = []

ciphertext = b'\x00'.hex()

A = 0

key = [36, 255, 255, 99, 114, 121, 112, 116, 111, 123, 119, 49, 82, 51, 100, 95, 101, 113, 117, 49, 118, 52, 108, 51, 110, 116, 95, 112, 114, 49, 118, 52, 99, 121, 63, 33, 125]

for A in range(35):
    prob = [0] * 256
    for k in range(256):
        iv = bytes([A + 3]) + bytes([255]) + bytes([k])
        iv = iv.hex()
        r = requests.get('https://aes.cryptohack.org/oh_snap/send_cmd/' + ciphertext + "/" + iv)
        key_stream = int.from_bytes(bytes.fromhex(json.loads(r.text)['error'].split(': ')[1]), byteorder='big')
        
        j = 0
        initSBox(box)
        key[0] = A + 3
        key[1] = 255
        key[2] = k

        for i in range(A + 3):
            j = (j + box[i] + key[i]) % 256
            swapValueByIndex(box, i, j)

            if i == 1:
                original0 = box[0]
                original1 = box[1]
        
        i = A + 3
        z = box[1]

        if z + box[z] == A + 3:

            if (original0 != box[0] or original1 != box[1]):
                continue
            keyByte = (key_stream - j - box[i]) % 256
            prob[keyByte] += 1

        higherPossibility = prob.index(max(prob))
    key.append(higherPossibility)
    print(key)

print(bytes(key[3:]))

## perform key recovery attack on ARC4 cipher
# using plaintext attack