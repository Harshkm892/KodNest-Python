#{key:value}, mutable, key can not be duplicate
student={
   ' name':"harsh",
   "name":"Rahul",
   "age":21,
   "course":"computerscience",
   "cgpa":7.7,
   "tech":["html","css","js","python","c++","sql"]


}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("course"))

student.popitem()
print(student.pop("age"))
del student
# print(student)



student={

   "name":"Rahul",
   "age":25,
   "course":"information technology",
   "cgpa":7.7,
   "tech":["python","c++","sql"]
}
student.setdefault("age",22)
print(student)

keys=["name","age","course"]
y=0
student=dict.fromkeys(keys,y)
print(student)

my_dict=student.copy()
print(my_dict)
my_dict.update({'name':"amit"})
print(my_dict)


#looop in dictionary
student={

   "name":"Rahul",
   "age":25,
   "course":"information technology",
   "cgpa":7.7,
  
}

for x in student:
   # print(x)

   print(f"{x}=>{student[x]}")

for x in student.items():
   print (x)


for x in student.keys():
   print( "keys=",x)


for x in student.values():
   print("value=",x)


   #nested dic
   student={
      "stu1":{
               "name":"Rahul",
                "age":25,
                "course":"information technology",
                "cgpa":7.7,
                  },

      "stu2":{
               "name":"amit",
                "age":22,
                "course":"ece",
                "cgpa":9.1,
                  }
  
}
print(student)
print(student["stu2"]["name"])
for x in student:
    print(x)
    for y in student[x]:
      print(y,student[x][y])
