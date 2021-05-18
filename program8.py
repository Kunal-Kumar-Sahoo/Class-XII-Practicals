# Write a recursive python program to test if a string is palindrome or not.

def check_palindrome(string):
    if len(string) == 1:
        return True
    if string[0] == string[-1]:
        return check_palindrome(string[1:-1])
    return False


if __name__ == "__main__":
    string = input("Enter a string: ")

    if string == '':
        print("Empty string !")
    else:
        if check_palindrome(string):
            print(f"{string} is a palindrome")
        else:
            print(f"{string} is not a palindrome")

