num = int(input("Enter a number: "))
for i in range(2, (num // 2) + 1):
    if num % i == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")


# cpp for loop
# flag =0
# for(i=2; i<=num; i++):
#     if(num % i == 0):
#         flag = 1
# break
# if(flag == 1):
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")