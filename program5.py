# Write a program to find the sum of all elements of a list using recursion.

def array_sum(array, n):
    if n == 0:
        return 0

    return array[n-1] + array_sum(array, n-1)


if __name__ == "__main__":
    arr = eval(input("Enter a list of numbers: "))
    sum = array_sum(arr, len(arr))
    print("Sum of the array:", sum)
