#Logical Operator (if condition)
#1 condition for the number divisible by both 2 and 3
a=18
if (a%2==0 & a%3==0):
    print("divisible")
else:
    print("not divisible")
    
    
#2 condition for the number divisible by 4 but not by 6
num=20
if (num%4==0 and num%6!=0):
    print("It is divisible")
else:
    print("not divisible")
    
#3 condition for first number less than the second number and greater than the third munber
num1=5
num2=25
num3=19
if (num1<num2 & num2>num3):
    print("True")
else:
    print("False")
    
    
#4 condition for the number between 20 and 40
x=23
if (20<x<40):
    print("between 20 and 40")
else:
    print("not between 20 and 40")
    
#5 condition for first  num even second num odd
a=2
b=7
if a%2==0 and b%2!=0:
    print("first num even and second num odd")
else:
    print("false")
    
#6 condition for the student score above 35 in all 4 subject
s1=45
s2=56
s3=62
s4=35
if (s1>=35 and s2>=35 and s3>=35 and s4>=35):
    print("Pass")
else:
    print("Fail")
    
#7 condition for the character a vowel 
char='e'
if char in "aeiouAEIOU" :
    print("vowels")
#8 condition for the character an upper case letter
char='H'
if ('A'<=char<='Z'):
    print("upper case")
    
char='S'
if char.isupper():
    print("Upper letter")
    
#9 condition for the character is digit 
num=6
if 0<=num<=9:
    print("Digit")
    
ch='8'
if ch.isdigit():
    print("digit")
    
#10 condition for the pin 4 digit long
num=4560
if 1000<=num<=9999:
    print("pin number")
    
pin=input("Enter PIN: ")
if len(pin)==4 and pin.isdigit():
    print("Valid PIN")
else:
    print("Invalid PIN")
    
    
#11 condition for the character an alphabet letter 
x='8'
if x.isalpha():
    print("True")
else:
    print("False")
    
x='E'
if ('A'<=x<='Z' or 'a'<=x<='z'):
    print("alphabets")
else:
    print("not an alphabets")
    
    
#12 condition for the character a symbol (non alphanumeric)
x='@'
if not x.isalnum():
    print("symbol")
else:
    print("not symbol")
    
#13 condition for the all three numbers equal to each other
a=5
b=5
c=5
if a==b==c:
    print("all 3 numbers are equal")
    
    
#14condition for the atleast two numbers among the three equal to each other
num1=6
num2=9
num3=6
if num1==num2 or num2==num3 or num3==num1 :
    print("At least two number equal")
    
#15 condition for the all three numbers different from each other
a=1
b=17
c=19
if a!=b!=c :
    print("True")
  
# Arthimetic Operators(if condition)

# 1 Program to add two numbers
n1=87
n2=99
if (n1+n2):
   print(n1+n2)
else:
   print("False")

# 2 program to display quotient and remainder after division
a = 7
b = 9
if a > 0 and b > 0:
    print("Quotient =", a // b)
    print("Remainder =", a % b)

# 3 program to find the total and average of 3 numbers
n1 = 5
n2 = 7
n3 = 8
total = n1 + n2 + n3
average = total / 3
if average > 0:
    print("Total =", total)
    print("Average =", average)

# 4 program to find the square of given number
n = 5
if n > 0:
    print("Square =", n*n)

# 5 program to find the cube of given number
a = 6
if a > 0:
   print("Cube=",a**3)	

# 6 program to find the sum of square and cube of given number
a = 5
if a > 0:
    print((a ** 2) + (a ** 3))

# 7 program to display the last digit of the given number
n = 2345
if n > 0:
    print("Last Digit =", n % 10)

# 8 program to swap 2 numbers
a = 5
b = 9
if True:
    a, b = b, a
    print(a, b)

# 9  program to swap 2 numbers without third variable
a = 5
b = 9
if a != b:
    a = a + b
    b = a - b
    a = a - b
    print("a =", a)
    print("b =", b)

# 10 calculate the total amount for the given fruits purchased
Apple = 3
kiwi = 4
Orange = 5
if Apple > 0 and kiwi > 0 and Orange > 0:
    total = (Apple * 50) + (kiwi * 100) + (Orange * 30)
    print("Total Amount =", total)

# 11 calculate the area of the circle
radius = int(input("Enter radius: "))
if radius > 0:
    area = 3.14 * radius * radius
    print("Area of Circle =", area)

# 12 Calculate the area of triangle
base = 15
height = 7
if base > 0 and height > 0:
    Area = (base * height) / 2
    print("Area =", Area)

# 13 calculate the time taken  using speed and distance
speed = 67.5
distance = 5.76
if speed > 0:
    print("The Time Taken =", distance / speed)

# 14 calculate the speed by using distance and time
distance=45.9
time=34.8
if time > 0:
   print("The Speed=",distance/time)

# 15 calculate the distance by using speed and time
speed=56.8
time=25.9
if speed > 0 and time > 0:
    print("The Distance=", (speed * time))
