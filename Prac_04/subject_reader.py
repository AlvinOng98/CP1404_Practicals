"""
CP1404/CP5632 Practical 4
Student Name: Alvin Ong Zhi Xiang
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():

    output = list_str()
    print(output)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list.append(parts)
    input_file.close()
    return data_list


# function converts list into a string
def list_str():

    mainList = [get_data()]
    strList = []
    outputStr = ""
    for subList in mainList:
        for l in subList:
            newStr = "{} is taught by {:12} and has {:>3} students".format(l[0], l[1], l[2])
            strList.append(newStr)
    for ele in strList:
        outputStr += '{}\n'.format(ele)
    return outputStr



main()
