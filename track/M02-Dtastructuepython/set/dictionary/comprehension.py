city=["delhi","mumbai","chemnnai","Bengaluru","Pune","Delhi"]
u_city={c.lower() for c in city}

print(u_city)
print(type(u_city))

number=[2,3,2,4,4,5,6]
unique_square=set()
for num in number:
    unique_square.add(num * num)
print(unique_square)    

unique_square={num*num for num in number}
print(unique_square)
print(type(unique_square))


number=[2,3,2,4,4,5,6]
square_list=[num*num for num in number]
square_set={num*num for num in number}
print(square_list)
print(square_set)

#dictionary 

number=[2,3,2,4,4,5,6]
cube_no = {}
for num in number:
    cube_no[num]=num*3
print(cube_no)    

cube_no={num:num*3 for num in number}
print(cube_no)
