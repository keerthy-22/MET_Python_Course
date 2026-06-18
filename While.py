# program to display the last digit of given number
n = int(input("Enter a Number: "))
while n >= 10:
    n = n % 10
print("Last Digit =", n)

# program to Remove the last digit of given number
n = int(input("Enter a Number: "))
n = n // 10
print("Number after removing last digit =", n)

# program to display one by one in reverse order
n = int(input("Enter a Number: "))
while n > 0:
    digit = n % 10
    print(digit,end=" ")
    n = n // 10

# program to count the digits in given numbers
n = int(input("Enter a Number: "))
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print("Number of Digits =", count)

# program to find the sum of digits in given numbers
n = int(input("Enter a Number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of Digits =", sum)

 # program to check last digit is even or not
n = int(input("Enter a Number: "))
while n > 0:
    last = n % 10
    if last % 2 == 0:
        print("Last Digit is Even")
    else:
        print("Last Digit is Odd")
    break

# program to display only even digits in the given number
n = int(input("Enter a Number:"))
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit)
    n = n // 10

# program to find the sum of the even digits in the given number
n = int(input("Enter a Number"))
sum = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum = sum + digit
    n = n // 10
print("Sum of Even Digits =", sum)

# program to count even digits in the given numbers
n = int(input("Enter a Number: "))
count = 0
while n > 0:
    if (n % 10) % 2 == 0:
        count = count + 1
    n = n // 10
print("Count of Even Digits =", count)

# program to find the largest digit in the given number
n = int(input("Enter a Number: "))
count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count = count + 1
    n = n // 10
print("Count of Even Digits =", count)

# program to find the smallest digit in the given number
n = int(input("Enter a Number: "))
small = 9
while n > 0:
    if n % 10 < small:
        small = n % 10
    n = n // 10
print("Smallest Digit =", small)
# program to find factorial value for each digit in the given number
n = int(input("Enter a Number: "))
while n > 0:
    digit = n % 10
    fact = 1
    i = 1
    while i <= digit:
        fact = fact * i
        i = i + 1
    print("Factorial of", digit, "=", fact)
    n = n // 10
# program to display square and cube values for each digit in the given number
n = int(input("Enter a Number: "))
while n > 0:
    d = n % 10
    print("Digit =", d)
    print("Square =", d ** 2)
    print("Cube =", d ** 3)
    n = n // 10

# program to display only prime digits in the given number
n = int(input("Enter a Number: "))
while n > 0:
    d = n % 10
    if d == 2 or d == 3 or d == 5 or d == 7:
        print(d,end=" ")
    n = n // 10