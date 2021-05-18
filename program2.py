# Write a program to check a number whether it is palindrome or not.

number = int(input("Enter a number: "))
temp = number

res = 0
while temp > 0:
    rem = temp % 10
    res = (res * 10) + rem
    temp //= 10

if res == number:
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is not a Palindrome.")
