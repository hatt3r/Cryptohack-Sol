from pwn import xor

print(xor("label",13))
    

## xor function from the pwn library to apply an XOR operation on the string "label" with the integer 13. 
# The result of this operation is printed, 
# which will encode the string using the XOR cipher with the given key