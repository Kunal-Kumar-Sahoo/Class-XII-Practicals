# Write a program in python to check a number whether it is prime or not.

def check_prime(number):
    for factor in range(2, number): 
        if number % factor == 0:
            return False
    return True


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if number < 1:
        print("Prime and Composite numbers are valid only for Natural Numbers.")
    elif number == 1:
        print("1 is neither prime nor composite number.")
    else:
        if check_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is a composite number.")
