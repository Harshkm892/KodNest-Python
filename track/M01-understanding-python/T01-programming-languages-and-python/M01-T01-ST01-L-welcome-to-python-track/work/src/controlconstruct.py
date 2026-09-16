# if statement
#wap to check a person is eligible to vote or not
age=int(input("Enter the age ="))

if(age>=18):
    print(age, "Person  is eligible to vote")
else:
    print(age,"Person is not eligible to vote")

#if-else-if-ladder/     

marks = int(input("Enter Marks: "))
if(marks >= 90):
    print("grade A")
elif(marks > 80):
    print("grade B")
elif(marks > 70):
    print("grade C")
elif(marks > 60):
    print("grade D")
elif(marks > 35):
    print("grade F") 
else: 
    print("Fail")


free_tonight=True
friends_available=True
if(free_tonight):
    print("Go out for party")
    if(friends_available):
        print("Go out for party")
    else:
        print("go alone")   
else:
    print("not available for party")


    

