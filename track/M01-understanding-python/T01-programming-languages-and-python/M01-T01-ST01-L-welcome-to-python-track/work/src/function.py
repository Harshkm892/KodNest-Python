# add two no.
from operator import num
def add():
    a,b=10,20
    c=a+b
    print(c)
add()
 
#squar eof no.

def square(num):
    return num * num
n = 5
result = square(n)

print("Square =", result)

#largest of 2 no.

def largest(a, b):
    if a > b:
        return a
    else:
        return b

num1 = 10
num2 = 20

result = largest(num1, num2)

print("Largest =", result)

#No argument no return type
def add1():
    a,b=10,20
    c=a+b
    print(c)
add1()
#no argument + return type
def add2():
    a,b=10,20
    c=a+b
    return c
print(add2())

#argument + return value
def add(a,b):
    c=a+b
    print(c)
    return c
add(10,50)

#argument +return value
def add4(a,b):
    c=a+b
    return c
res= add4(100,200)
print(res)

#python return multiple value
def cal(a, b):
    a, b = a + b, a - b
    return a, b

sum, diff = cal(100, 50)

print(sum)
print(diff)        

      

