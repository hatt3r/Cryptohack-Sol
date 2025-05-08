from pwn import *
import binascii
import json


SERVER_URL = remote('socket.cryptohack.org', 13421)


def padding_oracle_attack(ct_hex):

    print("Received ciphertext (hex):", ct_hex)


    try:
        ct_bytes = binascii.unhexlify(ct_hex)  
    except (binascii.Error, TypeError) as e:
        print(f"Error decoding hex: {e}")
        return None

    block_size = 16  
    num_blocks = len(ct_bytes) // block_size
    

    decrypted_message = bytearray(len(ct_bytes))
    

    for block_index in range(num_blocks - 1, 0, -1):
        block_start = block_index * block_size
        block_end = block_start + block_size
        current_block = ct_bytes[block_start:block_end]
        previous_block = ct_bytes[block_start - block_size:block_start]


        intermediate = bytearray(block_size)
        padding = bytearray(block_size)
        
        for byte_index in range(block_size - 1, -1, -1):

            padding[byte_index] = block_size - byte_index
            

            for guess in range(256):
                modified_ct = bytearray(ct_bytes)
                modified_ct[block_start + byte_index] = guess ^ padding[byte_index] ^ intermediate[byte_index]
                

                response = send_padding_check_request(modified_ct)
                
                if response["result"]:
                    intermediate[byte_index] = guess ^ padding[byte_index]
                    decrypted_message[block_start + byte_index] = intermediate[byte_index] ^ previous_block[byte_index]
                    break


    return decrypted_message


def send_padding_check_request(ct_bytes):
    ct_hex = binascii.hexlify(ct_bytes).decode("utf-8")
    payload = {"option": "unpad", "ct": ct_hex}
    

    SERVER_URL.sendline(json.dumps(payload))  
    response = SERVER_URL.recvline().decode()  

    return json.loads(response)  

def attack():
    SERVER_URL.sendline(json.dumps({"option": "encrypt"}))  
    response = SERVER_URL.recvline().decode()
    ct_data = json.loads(response)
    ct_hex = ct_data["ct"]

    print(f"Ciphertext received: {ct_hex}")


    recovered_message = padding_oracle_attack(ct_hex)
    
    if recovered_message:
        print("Recovered Message:", recovered_message.decode("utf-8"))
    else:
        print("Failed to recover the message.")

if __name__ == "__main__":
    attack()

## my attempt at pad_thai challenge
# was unsuccessul