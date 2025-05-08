from itertools import product
from chacha2 import ChaCha20
def brute_force_key(iv1, iv2, msg_enc, flag_enc):
    known_plaintext_flag = b"crypto{"  # Part of the flag you know

    for key_guess in product(range(256), repeat=32):  
        key_guess = bytes(key_guess)


        c = ChaCha20()


        decrypted_flag = c.decrypt(flag_enc, key_guess, iv2)
        

        if decrypted_flag.startswith(known_plaintext_flag):
            print(f"Found matching key: {key_guess.hex()}")
            return key_guess  

    print("No key found!")
    return None

## the encryption containing chacha20 stream algo from the chacha20.py
# is used to decrypt here as well