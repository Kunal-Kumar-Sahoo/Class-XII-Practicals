# Write a program to display ASCII code of a character and vice versa.

while True:
    print(
"""
Enter one of the choices: 
1: To print ASCII value of a character.
2: To print Character of a particular ASCII value.
3: To exit out of the program.
"""
    )
    option = int(input(':'))

    try:
        if option == 1:
            character = input("Enter a character: ")
            print(f"ASCII value of {character}: {ord(character)}")
        elif option == 2:
            ascii_value = int(input("Enter an ASCII value: "))
            print(f"Character for the given ASCII value {ascii_value}: {chr(ascii_value)}")
        elif option == 3:
            break
        else:
            print("Invalid  choice")

    except Exception as e:
        print(e)
