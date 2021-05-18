# Write a function SwapNumbers( ) to swap two numbers and display the numbers before swapping and after swapping.

def SwapNumbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp

    return num1, num2


if __name__ == "__main__":
    num1, num2 = input("Enter two numbers seperated by ',': ").split(',')
    num1, num2 = int(num1), int(num2)
    print(f"Original numbers: {num1}, {num2}")
    num1, num2 = SwapNumbers(num1, num2)
    print(f"After Swapping: {num1}, {num2}")

