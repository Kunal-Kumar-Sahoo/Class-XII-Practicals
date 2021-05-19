# Write a program to write those lines which have the character 'p' from one text file to another text file.

input_file = open("text-folder/input.txt", 'r')
output_file = open("text-folder/output.txt", 'a')

linesList = input_file.readlines()

for i in linesList:
    if i.lower().startswith('p'):
        writer = output_file.write(i)
print("Files written successfully !")
input_file.close()
output_file.close()
