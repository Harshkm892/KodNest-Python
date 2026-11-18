class Student:
    def __init__(self,name,age,gender,marks):
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

   
        # print("studing python and java")
        print(f"{self.name} is studying {self.age} years")
    def play(self):
        print(f"{self.name} is playing {self.age} years")

    def revision(self):
        print("revise the previous topic")

s1=Student("harsh",21,"male",95)   
print(f"Name:{s1.name}\nAge:{s1.age}\nMarks:{s1.marks}")     

s2=Student("Satyam",23,"male",85)   
print(f"Name:{s2.name}\nAge:{s2.age}\nMarks:{s2.marks}") 

s1.revision()
s2.play()
s2.revision()