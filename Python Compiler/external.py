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

def decisions():
    os.system('cls')
    typewriter("Wellcome to Decisions in Python, Enjoy :D")
    time.sleep(.5)
    os.system('cls')
    print("EXPLANATION:")
    typewriter("\tPython uses if, elif, and else statements to let your program make decisions. An if statement checks a")
    typewriter("\tcondition, and if that condition is true, Python runs the code inside it. If the condition is false,")
    typewriter("\tPython skips it. When you need to check more than one possible condition, you use elif, which means")
    typewriter("\t\"else if.\" Python goes through each condition in order until one of them is true. If none of the if")
    typewriter("\tconditions are true, the else block runs as the final fallback. This structure allows your program to")
    typewriter("\trespond differently depending on the situation, making your code more flexible and interactive.")
    time.sleep(1)
    while True:
        name = input("\nChoose below which example you want to shown :D\n\tA. if\n\tB. if + else\n\tC. if + elif + else\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            iff()         
        elif name == 'b':
            os.system('cls')
            if_else()           
        elif name == 'c':
            os.system('cls')
            if_elif_else()
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")

def loops():
    os.system('cls')
    typewriter("Wellcome to Loops in Python, Enjoy :D")
    time.sleep(.5)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. For Loop\n\tB. While Loop\n\tC. Loop Controls\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            for_loop()         
        elif name == 'b':
            os.system('cls')
            while_loop()           
        elif name == 'c':
            os.system('cls')
            loop_control()
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")

    
