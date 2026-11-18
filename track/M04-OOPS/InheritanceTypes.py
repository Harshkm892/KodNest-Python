#single inheritance => one child class inherits from parents classs
class Vehicle:
    def start(self):
        print("vehicle start")

class Car(Vehicle):
    pass
c=Car()
c.start()      

class Engine:
    def engine_type(self):
        print("petrol Engine")

class Wheels:
    def wheel_count(self):
        print("4 wheels")

class Car(Engine,Wheels):
    pass

c=Car()
c.engine_type()
c.wheel_count()

class Vehicle:
    def start(self):
        print("vehicle starts")
class Car(Vehicle):
    def driver(self):
        print("car drivers")

class SportsCar(Car):
    def speed(self):
        print("very fast")
s=SportsCar()
s.start()
s.driver()
s.speed()



