from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

with open('privacy_enhanced.pem', 'rb') as key_file:
    pem_data = key_file.read()

private_key = serialization.load_pem_private_key(pem_data, password=None)

private_exponent = private_key.private_numbers().d

print(private_exponent)

##This code reads an RSA private key from a PEM file and extracts its private exponent. 
# It begins by importing required modules from the cryptography library. 
# The PEM file, containing the private key, is opened in binary read mode, and its data is read into pem_data. 
# The serialization.load_pem_private_key function loads the private key object, assuming it is not password-protected. 
# Using the .private_numbers() method, the private exponent (d) is extracted and printed.
# This is typically used in cryptographic operations where specific RSA key parameters are required.