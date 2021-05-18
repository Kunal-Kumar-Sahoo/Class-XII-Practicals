# Write a program to print fibonacci series using recursion.

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)


if __name__ == "__main__":
    no_of_terms = int(input("Enter number of terms: "))

    if no_of_terms < 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci series: ")
        for i in range(no_of_terms):
            print(fibonacci(i), end=" ")
        print()

