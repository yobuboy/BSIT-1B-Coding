from internal import *
import os
import time

def introduction():
    os.system('cls')
    typewriter("Wellcome to Introduction of Python, Enjoy :D")
    time.sleep(.5)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. What is Python?\n\tB. Why is Python good for beginners?\n\tC. How to use this compiler?\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            one()         
        elif name == 'b':
            os.system('cls')
            two()           
        elif name == 'c':
            os.system('cls')
            three()
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")

def basics():
    os.system('cls')
    typewriter("Wellcome to Basics in Python, Enjoy :D")
    time.sleep(.5)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. Printing\n\tB. Variables\n\tC. Input\n\tD. Operators\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            prints()         
        elif name == 'b':
            os.system('cls')
            variables()           
        elif name == 'c':
            os.system('cls')
            inputs()
        elif name == 'd':
            os.system('cls')
            operators()
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")
