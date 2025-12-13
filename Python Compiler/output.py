from external import *
from internal import *
import time
import os

os.system('cls')
typewriter("Hello, programmer!")
time.sleep(.5)
name = user_name()
typewriter(f"\nWellcome {name} to the Python Learning Compiler\n")
time.sleep(1)
typewriter("Learn Python easily, understand each topic clearly, and start coding with confidence.\n")
time.sleep(2)
print("Let\'s begin!")
time.sleep(1)
input("\npress enter if you are ready!: ")
os.system('cls')

while True:
    name = input("Choose from the selection below :D\n\tA. Introduction\n\tB. Basics\n\tC. Decisions\n\tD. Loops\n\tE. Collections\n\tF. Functions\n\tG. Modules\n\tH. Mini Projects\n\tI. Quiz Section\n\tX. Exit\nType here ---> ").lower()
    if name == 'a':
        introduction()
    elif name == 'b':
        basics()
    elif name == 'c':
        decisions()
    elif name == 'd':
        loops()
    elif name == 'e':
        collections()
    elif name == 'f':
        functiosss()
    elif name == 'g':
        moduless()
    elif name == 'h':
        mini_proj()
    elif name == 'i':
        quiz_sect()
    elif name == 'x':
        break
    else:
        print("Invalid input!")
