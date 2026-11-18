employees=[
    {"employee_id":"E101", "name":"harsh","department":"Development"},
    {"employee_id":"E102", "name":"alok","department":"support"},
    {"employee_id":"E103", "name":"satyam","department":"testing"}
]
print(employees)

employee_by_id={}
for employe in employees:
    employee_id=employe["employee_id"]
    employee_by_id[employee_id]=employe
print(employee_by_id)