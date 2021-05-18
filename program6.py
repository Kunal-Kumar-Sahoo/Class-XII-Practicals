# Write a program to calculate the factorial of an integer using recursion.

def factorial(number):
    """
    Returns factorial of the parameter passed.
    """
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial of negative numbers do not exist")

    else:
        result = factorial(num)
        print(f"{num}! = {result}")
