from os import name
print("hashing")
print(hash(10))
print(hash("hello"))
print(hash(3.14))
print(hash(10.0))
print(hash((1,2,3)))
print(hash(True))


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        def __hash__(self):
            return hash((self.name,self.age))
s1 = Student("harsh",25)  
print(s1)
print(hash(s1))          
    

