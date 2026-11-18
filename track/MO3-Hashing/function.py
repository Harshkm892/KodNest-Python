c=30
def add():
    global a
    a=10
    b=20 #local variable
    print(a+b)
    print(c) #global variable
add()
print(c)    


x=100
def display():
    x=50
    print("Local x:",x)
    display()
    print("Global x:",x)

x=10  #global variable
def display():
    print(x)
    # x=20 # local variable
display()
x=20
print(x)    

def add(a,b):
    print(a+b)

def add(a,b,c):
    print(a+b+c)
def add(a,b,c=0,d=0):
    print(a+b+c+d)

add(10,20)   
add(10,20,30) 
add(10,20,30,40)


  
