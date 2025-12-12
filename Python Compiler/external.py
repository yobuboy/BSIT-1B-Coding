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
    decs_exple()
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

def collections():
    os.system('cls')
    typewriter("Wellcome to Collections in Python, Enjoy :D")
    time.sleep(.5)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. Summary Table\n\tB. List\n\tC. Tuple\n\tD. Set\n\tE. Dictionary\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            summ_list()        
        elif name == 'b':
            os.system('cls')
            listss()           
        elif name == 'c':
            os.system('cls')
            tuplesss()
        elif name == 'd':
            os.system('cls')
            setss()
        elif name == 'e':
            os.system('cls')
            dictss()
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")

def functiosss():
    os.system('cls')
    typewriter("Wellcome to Function in Python, Enjoy :D")
    time.sleep(.5)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. Built-in Functions (already provided by Python)\n\tB. User-Defined Functions (functions you create)\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            built_in()         
        elif name == 'b':
            os.system('cls')
            user_def()           
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")

def moduless():
    os.system('cls')
    typewriter("Wellcome to Modules in Python, Enjoy :D")
    time.sleep(.5)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. math\n\tB. random\n\tC. datetime\n\tD. os\n\tE. sys\n\tF. statistics\n\tG. json\n\tH. Summary Table\n\tX. Exit\nType here ---> ").lower()
        if name == 'a':
            os.system('cls')
            maths()         
        elif name == 'b':
            os.system('cls')
            randoms()
        elif name == 'c':
            os.system('cls')
            datetimes()
        elif name == 'd':
            os.system('cls')
            osss()
        elif name == 'e':
            os.system('cls')
            sysss()
        elif name == 'f':
            os.system('cls')
            statistics()
        elif name == 'g':
            os.system('cls')
            jsons()
        elif name == 'f':
            os.system('cls')
            sumbless()        
        elif name == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Invalid input!")
