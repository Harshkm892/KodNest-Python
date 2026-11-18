#operator overloading - + -> dunder method__

class Student:
    def __init__(self,marks):
        self.marks=marks

    def __add__(self,other):
        return self.marks + other.marks

    def __mul__(self,other):
        return self.marks * other.marks

s1= Student(20)
s2=Student(40)

print(s1+s2)
print(s1*s2)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        return self.age > other.age

p1= Person("harsh",22)
p2=Person("alok",26)

if p1 > p2:
    print(f"{p1.name}gives treat")
else:
    print(f"{p2.name}gives treat")    

