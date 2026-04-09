'''
def cubeVolume (sideLength):
    if sideLength >= 0 :
        return sideLength ** 3
    else :
        return 0
ruselt=cubeVolume(-3)     
print (ruselt)
'''
'''
# function to find pyramed volume with squre base
# l and h must be positive
# pyramed volume = Base area * hight * (1/3)
def pyramedVolume (l,h):
    if l >= 0 and h >=0 :  
        return (l*l)*h*(1/3)  
    else :
        return 0
    
ruselt=pyramedVolume(2,3)     
print (ruselt)
'''

  
''' 
def isprime(n):
    if n<=1:
       return False 
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
        
    return True
ruselt= isprime(3)
print(ruselt)
'''
'''
import math
n= int(input("Enter a number: "))

def sqrRoot(n):
    root = math.sqrt(n)
    if root.is_integer():
        return int(root)
    else:
        return "it dose not have  perfect squre"
    
ruselt=sqrRoot(n)
print (ruselt)
'''
'''
def boxString (contentes):
    n=len(contentes)
    print("-" * (n+2))
    print("!"+ contentes+"!")
    print("-" * (n+2))
    
bxoString ("Wajd Almaqrashi")
'''
'''
#Write a function table(n) that prints multiplication table of a number.

def table(n):
    for i in range(1,13):
        print( n,"X", i, "=", n*i)
        i+= 1
    
table(5)
'''
'''
#Write a function reverse_word(word) that returns the reversed word.

def reverse_word(word):
    reverse=""
    for i in range (len(word)-1, -1, -1):
        reverse= reverse+ word[i]
    return reverse
print(reverse_word("wajd"))
'''
'''
#  Write a function factorial(n) that returns factorial of a number.
def factorial(n):
    x=1
    for i in range(1, n+1):
        x *=i
    return x

ruselt=factorial(3)
print(ruselt)        
'''
'''
#Write a function Fibonacci Number
def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,n):
       x=a+b
       print(x)
       a=b
       b=x
    return"-------end----------"
     
print(fibonacci(9))
'''
'''
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
       print(a, end="")
       a, b = b, a+b
       
    return" "
     
print(fibonacci(7)) 
'''
'''
a=0
b=1
print(a)

for i in range (5):
    temp=a
    a = b
    b = b + temp
    
    if a>7:
        break
    else:
        print(a)
'''
'''
# Write a function sum_squares(n) that returns 1^1 + ... + n^n .

def sum_squares(n):
    summ=0
    for i in range (n+1):
        res= i**i
        summ+=res
        
    return summ
print (sum_squares(3))
'''