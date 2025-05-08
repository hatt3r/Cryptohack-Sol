from pwn import * # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

to_send = {
    "decoded": "0x6265726e6172645f696e74657265737465645f68756765"
}
json_send(to_send)

json_recv()

##This script connects to a remote server at socket.cryptohack.org on port 13377 
# and interacts by exchanging JSON-encoded messages. 
# It defines functions to receive (json_recv()) and send (json_send(hsh)) JSON data. 
# The script first retrieves an encoded message from the server, prints its type and value, 
# then decodes a specific string (e.g., 0x6265726e6172645f696e74657265737465645f68756765) and sends it back.