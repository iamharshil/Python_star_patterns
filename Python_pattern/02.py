# -----------------------My SOLUTION--------------------------------
num = int(input("Enter raws: "))


for i in range(0, num+1, 2):
    for j in range(1, i+2):
        print("#", end=" ")
    print()

#In my loop range fuction will skip likes like if i say 3 it will print 1 and three so bottom one is right.



num = int(input("Enter raws: "))  #took raws
k = 1

for i in range(1, num+1):   #printing total raw
    for j in range(1, k+1): #printing raw with each time 1 extra and adding 2 into k each time so k = 2, #; k = 4, ###; k=6, #####
        print("#", end=" ")
    k = k+2
    print()