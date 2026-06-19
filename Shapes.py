#Square
for row in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print()
print("--------------")
counter = 1
for row in range(1,6):
    for col in range(1,6):
        print(counter,end = " ")
        counter = counter+1
    print()
print("--------------")
for row in range(1,4):
    for col in range(1,5):
        print("*",end=" ")
    print()
print("--------------")
counter = 1
for row in range(1,4):
    for col in range(1,5):
        print(counter,end=" ")
        counter = counter + 1
    print()
print("--------------")
counter = 1
for row in range(1,5):
    for col in range(1,4):
        print(counter,end=" ")
        counter = counter + 1
    print()
print("--------------")
cols = 1
for row in range(1,6):
    for col in range(1,cols+1):
        print("*",end= " ")
    cols += 1
    print()
print("--------------")
counter = 1
cols = 1
for row in range(1,6):
    for col in range(1,cols+1):
        print(counter,end= " ")
        counter += 1
    cols += 1
    print()
print("--------------")
