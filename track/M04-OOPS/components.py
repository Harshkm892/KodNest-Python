class Student:
    #class attr-classname or object ref
    company="Kodnest Technologies"
    #Instance attribute-self or obj ref
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company

    #Instance method - using self reference ,abj ref
    def study(self):
        print(f"{self.name} is studying")  

    def getdetails(self):
        print("Name:",self.name) 
        print("Age:",self.age)
        print("Company:",self.company)

    def trip(self):
        print(f"{self.name} goes for a trip")

s1 = Student("Rahul",28,"Kodnest")

s1.study()
s1.getdetails()

print("\n")
s2=Student("Alok",22,"kodnest")
print(s2.name)
s2.study()
s2.getdetails( )

print(s1.company)
print(Student.company)
