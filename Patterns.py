for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("-------------")
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()
print("-------------")
for i in range(5):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()
print("-------------")
for i in range(1,6):
    for j in range(1,6):
        if i%2 == 0:
           print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print("-------------")
for i in range(1,6):
    for j in range(1,6):
        if j%2 == 0:
           print("0",end=" ")
        else:
            print("1",end=" ")
    print()
print("-------------")
for i in range(5):
    for j in range(5):
        print(chr(65+j),end=" ")
    print()
print("-------------")
for i in range(5):
    for j in range(5):
        print(chr(65+i),end=" ")
    print()
print("-------------")
for i in range(5):
    for j in range(5):
        print(chr(69-j),end=" ")
    print()
print("-------------")
for i in range(5):
    for j in range(5):
        print(chr(69-i),end=" ")
    print()