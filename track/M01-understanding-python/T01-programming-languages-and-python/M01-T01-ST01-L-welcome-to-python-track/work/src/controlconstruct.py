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

#wap to accept a no.from 1 to 7 and use match case to print corresponding day of the week
day =int(input("enter the no. between 1 to 7 "))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("saturday")
    case 7: print("sunday")
    case _: print("Invalid")

#match case with multiple cases/ wap that accept

month = int(input("enter the month number(1-12)"))
match month:
    case 3|4|5 :
        print("Summer")
    case 6|7|8 :
        print("Monsoon")
    case 9|10|11:
        print("winter")
    


 