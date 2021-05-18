# Write a program to generate random numbers between 1 to 6 and check whether a user won a lottery or not.

from random import randint

def lottery_number():
    token = randint(1, 6)
    return token


if __name__ == "__main__":
    number = lottery_number()
    count = 1
    while True:
        guess = int(input("Guess a number between 1 and 6: "))
        if guess == number:
            print(f"Congratulations! You guessed the number in {count} attempts.")
            break
        elif guess < number:
            print("Guess a bit higher.")
            count += 1
        else:
            print("Guess a bit lower.")
            count += 1



