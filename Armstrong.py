#Armstrong Code For 3-digit
n = int(input("Enter a Number: "))
temp = n
sum = 0
while n > 0: 
    rem = n % 10
    sum = sum + rem ** 3
    n = n // 10
if temp == sum:
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")
print("---------------------------------")
#Armstrong Code For 4-digit
n = int(input("Enter a Number: "))
temp = n
sum = 0
while n > 0: 
    rem = n % 10
    sum = sum + rem ** 4
    n = n // 10
if temp == sum:
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")
print("---------------------------------")
#Armstrong Code For digits
n = int(input("Enter a Number: "))
temp = n
count = 0
while temp > 0: 
    count = count + 1
    temp = temp // 10
temp = n
sum = 0
while temp > 0: 
    digit = temp % 10
    power = 1
    i = 0
    while i < count:
        power = power * digit
        i = i + 1
    sum = sum + power
    temp = temp // 10
if sum == n:
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")