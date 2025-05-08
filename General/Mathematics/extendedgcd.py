def gcdExtended(a, b): 

    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
    
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 
     

a = int(input("a is "))
b = int(input("b is "))
g, x, y = gcdExtended(a, b)
print("x",x,"y",y) 
print("gcd(", a , "," , b, ") = ", g)

##the Extended Euclidean Algorithm to find the greatest common divisor (GCD) of two integers a and b, 
# as well as coefficients x and y such that 
# 𝑎⋅𝑥+𝑏⋅𝑦=GCD(𝑎,𝑏) a⋅x+b⋅y=GCD(a,b). 
# It uses a recursive approach to compute the GCD, updating x and y accordingly. 
# The base case occurs when a is zero, returning the GCD as b with coefficients 0 and 1. 
# For other cases, it recursively calls itself to reduce the problem and calculate the coefficients, 
# ultimately returning the GCD along with x and y