class Student:
    def __init__(self, sid,name,fee):
        self.sid = sid
        self.name = name
        self.fee = fee
    def display(self):
        print("Student ID:",self.sid)
        print("Student Name:",self.name)
        print("Student Fee:",self.fee)
s1 = Student(101,"Keerthy",50000)
s1.display()
s2 = Student(102,"Kavya",60000)
s2.display()
