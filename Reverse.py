n = int(input("Enter a Number: "))
rev = 0
while n > 0: 
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("The reversed number is:", rev)
print("---------------------------------")
n = int(input("Enter a Number: "))
sum = 0
while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10
print("The sum of digits is:", sum)