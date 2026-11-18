number=[[1,2,3,4], [5,6,7,8,9]]
print(number)

print(number[0])
print(number[0][2])
print(number[1][2])


#traverse

student_marks=[
    [78,88,67],
    [72,88,95],
    [85,64,67]
]

for marks in student_marks:
   
    for m in marks:
        print(m)
        # print(marks)


# -------dictionary-->list------------
student={
    "development":["harsh","alok"],
    "Testing": ["rahul","rohit"]
}
for dept,emp in student.items():
    print(dept,emp)
    for e in emp:
        print(e)

# -----------list->dictionary------------

student=[

   { "name":"harsh",
    "marks":[72,73,89,56]
    },
     { "name":"Alok",
    "marks":[72,78,69,56]
    }
]
for stu in student:
    print(stu["name"])
    for m in stu["marks"]:
        print(m)

   