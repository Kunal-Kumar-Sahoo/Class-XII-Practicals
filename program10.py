# Write a program to count the number of vowels present in a text file.

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0

file = open("text-folder/input.txt", 'r')

text = file.read()

for character in text:
    if character.lower() in vowels:
        vowel_count += 1

print(f"Number of vowel-occurence: {vowel_count}")

file.close()
