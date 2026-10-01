#     *
#     *
# * * * * *
#     *
#     *

n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if(j==n//2 or i==n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
