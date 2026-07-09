class BigThreeNumber:
    def __init__(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
        self.num3 = int(input("Enter third number: "))
    def find_biggest(self):
        if self.num1 >= self.num2 and self.num1 >= self.num3:
            print("Biggest number is:", self.num1)
        elif self.num2 >= self.num1 and self.num2 >= self.num3:
            print("Biggest number is:", self.num2)
        else:
            print("Biggest number is:", self.num3)
b1 = BigThreeNumber()
b1.find_biggest()
