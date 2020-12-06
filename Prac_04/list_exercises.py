"""
CP1404 2020 Practical 4
Student Name: Alvin Ong Zhi Xiang
lists exercises
"""

MAX_INPUT = 5


def main():

    numbers = num_input()
    first = numbers[0]
    last = numbers[-1]
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers)/MAX_INPUT
    print("The first number is {}".format(first))
    print("The last number is {}".format(last))
    print("The smallest number is {}".format(smallest))
    print("The largest number is {}".format(largest))
    print("The average of the numbers is {}".format(average))


def num_input():

    numbers = []
    for i in range(0, MAX_INPUT):
        numInput = int(input("Please enter a number:"))
        numbers.append(numInput)
    return numbers


userNames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def user_input():

    username = input("Please enter your username:")

    return username


def user_check(username, userNames):

    if username in userNames:
        return True
    else:
        return False


main()