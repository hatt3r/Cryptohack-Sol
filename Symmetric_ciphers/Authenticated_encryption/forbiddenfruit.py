import requests


encrypt_url = 'https://aes.cryptohack.org/forbidden_fruit/encrypt/'
decrypt_url = 'https://aes.cryptohack.org/forbidden_fruit/decrypt/'

plaintext = 'CryptoHack'


response = requests.get(encrypt_url + plaintext)
data = response.json()


nonce = data['iv']
ciphertext = data['ciphertext']
tag = data['tag']
associated_data = data['associated_data']

decryption_response = requests.get(
    decrypt_url + f"{nonce}/{ciphertext}/{tag}/{associated_data}"
)

print(decryption_response.json())

##encypting and decrypting using web service 