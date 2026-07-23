class Employee:
    def __init__(self, emp_id, name, monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        print("\n------ Employee Details ------")
        print("Employee ID     :", self.emp_id)
        print("Employee Name   :", self.name)
        print("Monthly Salary  : ₹", self.monthly_salary)
        print("Annual Salary   : ₹", self.calculate_annual_salary())


# Get input from the user
emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
monthly_salary = float(input("Enter Monthly Salary: "))

# Create object
employee1 = Employee(emp_id, name, monthly_salary)

# Display details
employee1.display_details()
