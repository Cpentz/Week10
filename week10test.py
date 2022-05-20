import os


filePath = input("Enter directory path: ")
fileName = input("Enter file name: ")

name = input("Enter name: ")
address = input("Enter address: ")
number = input("Enter phone number: ")

completePath = filePath+fileName
if os.path.isfile(fileName):
    print("File Exists")
if os.path.isdir(filePath):
    print("Directory Exists")
if os.path.exists(completePath):
    print("Complete Path Exists")
print("Complete Path", completePath)
with open(completePath, 'w') as fileHandle:
    fileHandle.write(str(name + ', ' + address + ', ' + number))
with open(completePath, 'r') as fileHandle:
    data = fileHandle.read()
    print(data)