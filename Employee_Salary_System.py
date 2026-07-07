employees = {}

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Salary: "))
    employees[name] = salary

print("\nEmployees")
print(employees)

print("\nEmployee Names")
for name in employees.keys():
    print(name)

print("\nSalaries")
for salary in employees.values():
    print(salary)

name = input("\nEnter Employee Name: ")

if name in employees:
    salary = employees[name]

    hra = salary * 20 / 100
    da = salary * 10 / 100
    gross_salary = salary + hra + da

    print("\nEmployee Name :", name)
    print("Basic Salary  :", salary)
    print("HRA           :", hra)
    print("DA            :", da)
    print("Gross Salary  :", gross_salary)

else:
    print("Employee Not Found")
