# pyrefly: ignore[missing-import]
# import calculatormodule
# print( calculatormodule.add(10,30))


# square using normal function
numbers=[1,2,3,4,5]
def square(n):
    return n * n 

result = []
for i in numbers:
    result.append(square(i))

print(result)       


#even using normal function

def is_even(n):
    if n%2==0:
        return True
    else:
        return False    
even =[]
for i in numbers:
    if is_even(i):
        even.append(i)
print(even)                


def add(x,y):
    return x+y
sum_of_num =0
for i in numbers:
    sum_of_num = add(sum_of_num,i)
print(sum_of_num)    
