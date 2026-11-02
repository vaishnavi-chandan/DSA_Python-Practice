# Write a program to check whether the given number is palindrome or not.
num = int(input("Enter a number: "))
sum=0
n=num
while(n>0):
    sum=sum*10+(n%10)
    n//=10

print("The reverse of the number is:", sum)
if sum == num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")