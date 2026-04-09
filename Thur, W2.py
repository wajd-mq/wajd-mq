'''
fullName="Wajd Almaqrashi"

firstName = fullName.split( )[0]
secName = fullName.split(  )[1]

print(secName,firstName)
'''
'''
import re
text = "SplitStringByUpper"
result = re.split('(?=[A-Z])', text)
print(result)
'''
'''
width, length, height = map(int, input("Enter width, length and height: ").split())

print(width)
print(length)
print(height)
'''
'''
hour, minut =map(int, input("Enter a time [HH:MM] :").split(":"))

print('hour: ', hour)
print('minut: ', minut)
'''
'''
name, grade =input("Enter a name and grade: ").split()

print(name, grade)
'''
'''
balance=1000

def withdraw(amount):
    global balance
    if balance>= amount:
        balance = balance - amount
        
withdraw(350)
print("balance=  ", balance)
'''
'''
area= lambda x, y: x*y
print(area(3, 2))

a="wajdAlmaqrashi"
upper= lambda x: x.upper()
print(upper(a))


check = lambda x: "pos" if x>0 else "neg" if x<0 else "zero"
print(check(5))
print(check(-2))
print(check(0))
'''
'''
def func1(*args):
    for arg in args:
        print(arg)
        
func1(10, 20)
func1("Hi", 3.14, True)
func1()
func1(1, 2, 3, 4, 5, 6, 7)
'''
'''
def culculation(a, b):
    return a+b, a-b

res=culculation(40, 10)
print(res)
'''
'''
def show_employee(name, salary=9000):
    print("Name: ", name, ",Salary: ", salary)
    
show_employee("Ben", 1200)
show_employee("Jon")
'''
'''
def func1(a, b):
    def func2(i,j):
       return i+j
    return func2(a,b)+5 
print(func1(2,3))
'''
'''
def func1(a, b):
    def func2():
       return a+b
    return func2()+5 
print(func1(2,3))
'''
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
'''
'''
def summ_fun(n):
    if n==0:
        return 0
    return n+summ_fun(n-1)
print(summ_fun(10))
'''
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i))
'''




