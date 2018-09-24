limit = int(input("Enter the number : "))
for i in range(1,limit+1):
    for j in range(0,limit-i):
        print("1",end=" ")
    for k in range(0,i):
        print(i,end=" ")
    print(" ")
