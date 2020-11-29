"""
CP1404 2020 Practical 1
Student Name: Alvin Ong Zhi Xiang
Fixing broken program to determine score status
"""
import random


def main():

    score = user_score()
    output_result(score)


def output_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


def user_score():
    score = float(input("Enter score:"))
    return score


def random_score():
    score = random.randint(0, 101)
    return score

main()
