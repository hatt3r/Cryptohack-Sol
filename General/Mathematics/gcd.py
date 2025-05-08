def gcd(a, b):


    if (a == 0):
        return b
    if (b == 0):
        return a


    if (a == b):
        return a


    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


a = int(input("enter a "))
b = int(input("enter b "))
if(gcd(a, b)):
	print("GCD Of a and b is ", gcd(a, b))
else:
    print('not found')

##implementing GCD using euclidean algorithm
#finds the GCD by repeatedly reducing the problem 
# using the properties of subtraction gcd(a-b,b) or gcd(a,b-a)