# Write a python program to write student data in a binary file.

import pickle
import os

def setData():
    rollNumber = int(input("Enter roll number of the student: "))
    studentName = input("Enter name of the student: ")
    studentPercent = float(input("Enter percentage of the student: "))

    studentData = {'roll':rollNumber, 'name':studentName, 'percentage':studentPercent}

    return studentData


def writeData(filePath, studentRecords):
    file = open(filePath, 'ab')
    pickle.dump(studentRecords, file) 
    file.close()


if __name__ == "__main__":
    
    filePath = 'text-folder/binary-file.dat'
    studentRecords = [] 

    if os.path.exists(filePath):
        file = open(filePath, 'rb')
        previousRecords = pickle.load(file)
        studentRecords.append(previousRecords)
        file.close()

    totalStudents = int(input("Enter total number of students: "))
    for i in range(totalStudents):
        studentData = setData()
        studentRecords.append(studentData)
    file = open(filePath, 'ab')
    pickle.dump(studentRecords, file)
    file.close()
    print("Data written succesfully !")

