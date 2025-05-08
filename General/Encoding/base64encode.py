import base64
stringss = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"


print(base64.b64encode(bytearray.fromhex(stringss)))

##This code converts a hexadecimal string into a Base64-encoded string. 
# It uses bytearray.fromhex to convert the hexadecimal string stringss into a byte array. 
# The base64.b64encode function then encodes this byte array into a Base64 string, 
# which is printed as the result.
