# Write a program to count number of words in a file.

file = open("text-folder/input.txt", 'r')

text = file.read()
wordsList = text.split()

count = len(wordsList)
print(f"Total number of words: {count}")

file.close()
