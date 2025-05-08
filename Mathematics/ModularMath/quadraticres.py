from Crypto.Util.number import *
zn_ = [i for i in range(1,29) if GCD(29,i) == 1]
ints = [14,6,11]
for i in (zn_):
    for j in ints:
            for k in range(1,100):
                if(pow(i,2) -j == k*29):
                    print(i)
                    
                    
##trying to find integers i such that pow(i, 2) - j 
# is a multiple of 29 for given values in integer array ints 
# and printing the ones that are 