class Student:
    #class attr-classname or object ref
    company="Kodnest Technologies"
    
    def __init__(self,name,age):
        #Instance attribute-self or obj ref
        self.name=name
        self.age=age
       

    #Instance method - using self reference ,abj ref
    def study(self):
        a=10
        print(a)#Local attribute
        print(f"{self.name} is studying")  
#instance method
    def getdetails(self):
        print("Name:",self.name) 
        print("Age:",self.age)
        print("Company:",self.company)
#ststics method-classname,object
    @staticmethod
    def trip(self):
        print(f"{self.name} goes for a trip")
#class method-classname,object
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
        
Student.change_company("Kodnest Technologies pvt lmt")

s1=Student("rahul",20)
print(Student.company)
print(s1.name)
s1.study()
s1.getdetails()

print("\n")
s2=Student("Harsh",22)
print(s2.name)
s2.study(  )
