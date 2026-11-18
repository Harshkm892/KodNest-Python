class Student:
    college_name="ABC UNIVERSITY"

    def __init__(self,name,age,roll_number):
        self.name=name
        self.age=age
        self.roll_number=roll_number

    @classmethod
    def change_collagename(cls,new_name):
        cls.college_name=new_name  #modify class attributre using class method
    def attend_class(self):
        print(f"{self.name} from {Student.college_name} is attending the class.")

Student.change_collagename("AKGEC GHAZIABAD")
student1=Student("Amit",20,"S123")
student2=Student("priya",20,"s124")

student1.attend_class()
student2.attend_class()

print(Student.college_name)

student1.change_collagename("ABES COLLEGE")
print(Student.college_name)

student1.attend_class()
student2.attend_class()