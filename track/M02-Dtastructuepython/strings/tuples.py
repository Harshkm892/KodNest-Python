name = ("alice","bob","charlie","bob","david")
print(name,type(name),len(name))
print(name.count("bob"))
print(name.index("bob"))
print(name[3])
yn=name[0:3]
print(yn,type(yn))

#loop
for n in name:
    print(name)

#constructor
stu_info =tuple(["harsh",22,23000,True])
print(stu_info,type(stu_info))   

n=10
print(n,type(n))
numbers=1,2,3,4,5,
print(numbers,type(numbers))
# numbers[1]=200   #immutable

del numbers

age=[10,20]
age[1]=25
print(age)

#tuplw packing and unpacking

#unpacking
fruits=("apple","banana","cherry")
(f1,*f2)=fruits
print(f1)
print(f2,type(f2))

fruit1=("mango","papaya","orange")
(a1,a2,a3)=fruit1
print(a1)
print(a2)
print(a3)

#packing
a=10
b=20
c=30

numbers=(a,b,c)
print(numbers,type(numbers))
c=a+b
print(c,type(c))