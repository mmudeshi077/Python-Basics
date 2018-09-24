limit = int(input("Enter the limit :"))
looplimit = 2*(limit+1)+1
for i in range(1,looplimit):
    if i<limit+1 :
        for j in range(1,i-1):
            print(j,end=" ")
    else:
        for j in range(1,looplimit-i):
            print(j,end=" ")
    print(" ")
