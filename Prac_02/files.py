"""
CP1404/CP5632 - Practical 2
Student Name: Alvin Ong Zhi Xiang

Files
"""

out_file = open("name", 'w+')

with open("name", "w+") as name:
    name.write(input("Please enter your name:"))

output = out_file.read()
print("Your name is", output)
print("")
out_file.close()

in_file = open("numbers.txt", "r")
result = 0
for i in range(0, 2):
    num = int(in_file.readline())
    result += num
print(result)
print("")
in_file.close()

file = open("numbers.txt", "r")
total = 0
for line in file:
    num1 = int(line)
    total += num1
print(total)

