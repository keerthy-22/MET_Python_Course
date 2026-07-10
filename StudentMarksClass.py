class Student:
    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    # Method to display student details
    def display_details(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

    # Method to check pass/fail
    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


# Input from user
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
marks = int(input("Enter Marks: "))

# Create object
student1 = Student(name, roll_no, marks)

# Display details and result
student1.display_details()
student1.check_result()
