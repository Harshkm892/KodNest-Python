numbers=[1,2,3,4,5 ,3]
print(numbers[1:5])
print(numbers[3:])
print(numbers[-4 :-1])
print(numbers,type(numbers))
print(len(numbers))
print(numbers[3])

#using constructor
stu = list([1,2,3,4,True,"Abhi"])
print(stu,type(stu))

#adding element
num=[1,2,3,4,5]
num.append(6)
num.insert(0,3)
num.extend([10,20,30])
print(num)


#removing the element
num.pop()
num.pop(1)
num.remove(20)
num.clear()

print(num)


#changing element
numbers=[1,2,3,4,5,3]

numbers[5]=6
numbers[1:4]=[20,30,40]
print(numbers)

a=[1,2,3,4,4]
b=a.copy()

print(a.count(4))
print(b)
print(b.index(3)) #2

x=[2,4,1,3,8,5]
x.sort()
print(x)