#duct typing
class Cat:
    def sound(self):
        print("cat meows")

class Cow:
    def sound(self):
        print("cow Mows")

def make_sound(animals):
    animals.sound()  

ct=Cat()
cw=Cow()
make_sound(cw)
make_sound(ct)


class Googlepay:
    def pay(self):
        print("payment through google pay")
class Phonepay:
    def pay(self):
        print("payment through phone pay")        

class Craditcard:
    def pay(self):
        print("payment through cradit card")  

def process_payment(payment):
    payment.pay()

g=Googlepay()
p=Phonepay()    
c=Craditcard()

process_payment(g)
process_payment(p)
process_payment(c)