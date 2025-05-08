from Crypto.Util.number import *

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

print(long_to_bytes(integer))

##This code converts a large integer into its corresponding byte representation. 
# Using Crypto.Util.number, it takes the integer integer, which is a large numeric value, 
# and converts it to a byte array using the long_to_bytes function. 
# The resulting byte array is then printed. 
# This is often used in cryptographic applications where data needs to be represented as binary data.