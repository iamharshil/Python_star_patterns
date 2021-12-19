
num = int(input("Enter raws: "))

for i in range(0, num):
    for j in range(0,num - i - 1):
        print(end=" ")
    for i in range(0, i+1):
        print("#", end=" ")
    print()