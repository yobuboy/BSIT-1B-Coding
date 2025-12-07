from external import *
from internal import *
import time
import os

os.system('cls')
typewriter("Hello, programmer!")
time.sleep(.5)
typewriter("Wellcome to the Python Learning Compiler\n")
time.sleep(1)
typewriter("Learn Python easily, understand each topic clearly, and start coding with confidence.\n")
time.sleep(2)
print("Let\'s begin!")
time.sleep(1)
input("\npress enter if you are ready!: ")
os.system('cls')

while True:
    name = input("Choose from the selection below :D\n\tA. Introduction\n\tB. Basics\n\tC. Decisions\n\tD. Loops\n\tE. Collections\n\tF. Functions\n\tG. Modules\n\tH. Files\n\tI. Mini Projects\n\tJ. Quiz Section\n\tX. Exit\nType here ---> ").lower()
    if name == 'a':
        introduction()
    elif name == 'b':
        basics()
    elif name == 'c':
        pass
    elif name == 'd':
        pass
    elif name == 'e':
        pass
    elif name == 'f':
        pass
    elif name == 'g':
        pass
    elif name == 'h':
        pass
    elif name == 'i':
        pass
    elif name == 'j':
        pass
    elif name == 'x':
        break
    else:
        print("Invalid input!")