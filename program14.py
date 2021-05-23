# Write a python program to read student data from a binary file.

import pickle
import os


def displayData(student_records):
    for student in student_records:
        print(f"Roll number: {student['roll']}")
        print(f"Name: {student['name']}")
        print(f"Percentage: {student['percentage']}")
        print()
        

def readRecords(filePath):
    file = open(filePath, 'rb')
    while True:
        try:
            studentRecord = pickle.load(file)
            displayData(studentRecord)
        except EOFError:
            break
    file.close()


if __name__ == "__main__":
    filePath = "text-folder/binary-file.dat"

    if os.path.exists(filePath):
        readRecords(filePath)
    else:
        print("File not found!")
