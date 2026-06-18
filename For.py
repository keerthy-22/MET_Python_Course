# program to print 1 to 10 Numbers
for i in range(1,11):
    print(i,end=" ")

# program to print 10 to 1 Numbers
for i in range(10,0,-1):
    print(i,end=" ")

# program to display A-Z alphabets using ASCII Values
for i in range(65,91):
     print(chr(i),end=" ")

# program numbers 2,4,6,8,10
for i in range(2,11,2):
    print(i,end=" ")

# program numbers 15,12,9,6,3,0
for i in range(15,-1,-3):
     print(i,end=" ")

# program numbers 10,20,30,40,50
for i in range(10,60,10):
    print(i,end=" ")

# program numbers 100,80,60,40,20
for i in range(100,0,-20):
     print(i,end=" ")

# program lower case alphabets a to z
for ch in range(97,123):
     print(chr(ch),end=" ")

# program upper case alphabets Z to A 
for ch in range(90,64,-1):
     print(chr(ch),end=" ")

# program upper case alphabets A to Z
for ch in range(65,91):
     print(chr(ch),end=" ")

# program to print ASCII Values from a to z
for ch in range(97,123):
     print(chr(ch),end=" ")

# program to print ASCII Values from 0 to 9
for ch in range(48,58):
     print(chr(ch),end=" ")

# Program to display ASCII character set
for ch in range(0, 128):
    print(ch, chr(ch),end = " ")

# program to print square values for numbers 1 to 5
for i in range(1,6):
    print(i,"x",i,"=",i**2)

# program to print cube values for numbers 1 to 5
for i in range(1, 6):
    print(i,"x",i,"x",i,"=", i**3)

# program to find the sum of first N numbers
n = int(input("Enter N: "))
print("Sum =",sum(range(1, n+1)))
