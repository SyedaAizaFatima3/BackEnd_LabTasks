

file = open("example.txt", "r")

# Always close the file after using it
file.close()



file = open("example.txt", "r")

content = file.read()

print(content)

file.close()


file = open("example.txt", "r")

# Read first 10 characters
content = file.read(10)

print(content)

file.close()

file = open("example.txt", "r")

line = file.readline()

print(line)

file.close()


file = open("example.txt", "r")

line1 = file.readline()
line2 = file.readline()

print(line1)
print(line2)

file.close()


file = open("example.txt", "r")

lines = file.readlines()

print(lines)

file.close()

file = open("example.txt", "r")

# Each iteration reads one line
for line in file:

    print(line)

file.close()


file = open("example.txt", "r")

for line in file:

    # strip() removes extra spaces and \n
    print(line.strip())

file.close()

file = open("student.txt", "w")

file.write("My name is Ali.")

file.close()

file = open("student.txt", "w")

file.write("Name: Ali\n")
file.write("Age: 20\n")
file.write("Grade: A\n")

file.close()


name = "Ali"
age = 20

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Age: " + str(age) + "\n")

file.close()

students = [
    "Ali\n",
    "Ahmed\n",
    "Sara\n",
    "Ayesha\n"
]

file = open("students.txt", "w")

file.writelines(students)

file.close()



file = open("student.txt", "a")

file.write("University: UOL\n")

file.close()


file = open("student.txt", "a")

file.write("Semester: 4\n")
file.write("Department: IET\n")

file.close()


file = open("newfile.txt", "x")

file.write("This is a new file.")

file.close()

import os

if os.path.exists("student.txt"):

    print("File exists")

else:

    print("File does not exist")


import os

if os.path.exists("newfile.txt"):

    os.remove("newfile.txt")

    print("File deleted")

else:

    print("File does not exist")


