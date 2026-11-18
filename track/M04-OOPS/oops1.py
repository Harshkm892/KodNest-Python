class Student:
    name="harsh"
    age=21
    gender="male"
    def study(self):
        # print("studing python and java")
        print(f"{self.name} is studying {self.age} years")
    def play(self):
        print(f"{self.name} is playing {self.age} years")

    def revision(self):
        print("revise the previous topic")

s1=Student()
s2=Student()
s2.name="alok"
s2.age=22
print(f"name:{s1.name} age:{s1.age} gender:{s1.gender}")
print(s1.study())
print(s1.revision())
print(s2.name)


