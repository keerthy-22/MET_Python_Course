class OnlineCourse:
    def __init__(self, course_name, instructor, duration, fee):
        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.fee = fee
        self.enrolled_students = 0

    def enroll_student(self):
        self.enrolled_students += 1
        print("\nStudent enrolled successfully.")

    def display_details(self):
        print("\n------ Course Details ------")
        print("Course Name       :", self.course_name)
        print("Instructor        :", self.instructor)
        print("Duration          :", self.duration)
        print("Course Fee        : ₹", self.fee)
        print("Enrolled Students :", self.enrolled_students)


# User Input
course_name = input("Enter Course Name: ")
instructor = input("Enter Instructor Name: ")
duration = input("Enter Course Duration: ")
fee = float(input("Enter Course Fee: "))

# Create Object
course1 = OnlineCourse(course_name, instructor, duration, fee)

# Display Initial Details
course1.display_details()

# Enroll Students
n = int(input("\nEnter Number of Students to Enroll: "))

for i in range(n):
    course1.enroll_student()

# Display Updated Details
course1.display_details()
