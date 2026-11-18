class Employee:
    def __init__(self,empname,empage, empsalary,emprole):
        self.empname=empname
        self.empage=empage
        self.empsalary=empsalary
        self.emprole=emprole

        #Inherited method

    def displayinfo(self):
        print(f"Name: {self.empname}")
        print(f"Age: {self.empage}")
        print(f"Salary: {self.empsalary}")
        print(f"Name: {self.emprole}")

    #Method to be overriddendef display(self):
    def work(self):
        print("Employee is working")

    #child classs developer
class Developer(Employee):
        #overriding method
    def work(self):
            print("development Work")
        # specialized method

    def project(self,project_name):
            print(f"Developer is developing project: {project_name}")


   #child class tester
class Tester(Employee):
      #overriding method
    def work(self):
        print("development Work")
    def project(self,project_name):
            print(f"Tester is testing project: {project_name}")


dev= Developer("Alice",25,5000,"Developer")
test=Tester("bob",27,45000,"tester")

print("---Developer-----")
dev.displayinfo()
dev.work()
test.work()
test.project("Bank App")

print("---Developer-----")
dev.displayinfo()
dev.work()
test.work()
test.project("E-commerce App")





    


