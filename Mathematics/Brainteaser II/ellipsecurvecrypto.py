from Crypto.Cipher import AES
from hashlib import sha1
from Crypto.Util.Padding import unpad

shared_secret = 31087407633021917046588316360667560806162238688220407682282055483296128
key = sha1(str(shared_secret).encode('ascii')).digest()[:16]
iv = bytes.fromhex('64bc75c8b38017e1397c46f85d4e332b')

encrypted_flag = bytes.fromhex('13e4d200708b786d8f7c3bd2dc5de0201f0d7879192e6603d7c5d6b963e1df2943e3ff75f7fda9c30a92171bbbc5acbf')

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = cipher.decrypt(encrypted_flag)

print(f"Decrypted Data (raw): {decrypted_data.hex()}")

def check_and_strip_padding(data):
    prefix = b"crypto{"
    if data.startswith(prefix):
        padding_length = data[-1]
        if 0 < padding_length <= 16:
            return data[:-padding_length]
        else:
            raise ValueError("Manual padding removal failed.")
    else:
        try:
            return unpad(data, 16)
        except ValueError:
            print("Unpadding failed due to incorrect padding.")
            return None

flag_data = check_and_strip_padding(decrypted_data)

if flag_data:
    try:
        flag = flag_data.decode()
        print(f'FLAG: {flag}')
    except UnicodeDecodeError:
        print("Decrypted data does not form a valid string.")
else:
    print("Failed to recover the flag.")


## decrypting an AES encrypted flag using the shared secret and IV. 
# It first decrypts the data, then checks and strips padding before attempting to decode the flag.
# If successful, it prints the flag; 
# otherwise, it indicates failure.