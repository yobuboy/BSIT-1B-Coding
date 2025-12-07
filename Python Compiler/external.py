from internal import *
import os

def introduction():
    os.system('cls')
    while True:
        name = input("\tA. What is Python?\n\tB. Why is Python good for beginners?\n\tC. How to use this compiler?\n\tX. Exit").lower()
        if name == 'a':
            os.system('cls')
            print(one)
            continue
        elif name == 'b':
            os.system('cls')
            print(two)
            continue
        elif name == 'c':
            os.system('cls')
            print(three)
            continue
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")

