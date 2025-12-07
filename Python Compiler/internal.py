import os
import time
import sys

def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def one():
    os.system('cls')
    print("Python is a high-level, versatile programming language created by Dutch software engineer Guido van")
    time.sleep(.1)
    print("Rossum, who began its development in the late 1980s and released the first public version in 1991. Designed")
    time.sleep(.1)
    print("with an emphasis on readability and simplicity, Python uses clean, English-like syntax that makes it easier for")
    time.sleep(.1)
    print("beginners to learn while still offering powerful capabilities for experts. Van Rossum, often referred to as")
    time.sleep(.1)
    print("Python\'s \"Benevolent Dictator for Life\" (BDFL) until he stepped down from that role in 2018, drew inspiration")
    time.sleep(.1)
    print("from languages like ABC and aimed to create a language that encouraged clear, logical code. Over the years,")
    time.sleep(.1)
    print("Python has grown into one of the world\'s most popular languages, used across web development, data")
    time.sleep(.1)
    print("science, automation, artificial intelligence, and scientific computing, supported by a massive global")
    time.sleep(.1)
    print("community and an extensive ecosystem of libraries.")
    time.sleep(.1)
    print("=================================================================================================================\n")
    input("press enter to continue: ")
    os.system('cls')

def two():
    os.system('cls')
    print("Python is good for beginners because it is easy to read and understand. Its code looks simple, almost like")
    time.sleep(.1)
    print("normal English, so new learners don\'t get confused. It also has fewer rules and symbols, making it easier to")
    time.sleep(.1)
    print("write and fix mistakes. Python has a big community, which means there are many tutorials and examples")
    time.sleep(.1)
    print("available online for students. It can also be used for many things like making websites, automating tasks, or")
    time.sleep(.1)
    print("working with data, so beginners can explore different projects without changing languages. Overall, Python")
    time.sleep(.1)
    print("is simple, flexible, and beginner-friendly, which makes it a great first programming language.")
    time.sleep(.1)
    print("=================================================================================================================\n")
    time.sleep(.1)
    input("press enter to continue: ")
    os.system('cls')

def three():
    os.system('cls')
    print("This is a python compiler that helps you to learn how to program using python as a programming language by")
    time.sleep(.1)
    print("choosing an option after you run the program.")
    time.sleep(1)
    print("\nThis compiler also have a quiz to determine if you really learn something in this python learning journey.")
    time.sleep(3)
    print("\nGOODLUCK!!")
    time.sleep(.1)
    input("press enter to continue: ")
    os.system('cls')

def prints():
    os.system('cls')
    print("EXPLANATION:")
    typewriter("\tprint() is a built-in function in Python that is used to display information on the screen.")
    typewriter("\tAnything you put inside print() will be shown to the user when the program runs.")
    time.sleep(1)
    while True:
        name = input("\nChoose from the selection below :D\n\tA. Printing Text\n\tB. Printing Numbers\n\tC. Printing Text with Numbers\n\tX. Exit\nType here ---> ")
        if name == 'a':
            os.system('cls')
            typewriter("This is how printing text works in python")
            typewriter("INPUT:\n\tprint(\"Hello World\")\n\nOUTPUT:\n\tHello World")
            time.sleep(2)
            input("\npress enter to try how to use print: ")
            os.system('cls')
            typewriter("Type \'exit\' if you want to leave.\n")
            time.sleep(2)
            while True:
                user_code = input(">>> ")
                if user_code.lower() == "exit":
                    typewriter("Exiting compiler...")
                    break               
                try:
                    exec(user_code)
                except Exception as e:
                    print("Error:", e)
            os.system('cls')
        elif name == 'b':
            os.system('cls')
            typewriter("This is how printing numbers works in python")
            typewriter("INPUT:\n\tprint(100)\n\nOUTPUT:\n\t100")
            time.sleep(2)
            input("\npress enter to try how to use print: ")
            os.system('cls')
            typewriter("Type \'exit\' if you want to leave.\n")
            time.sleep(2)
            while True:
                user_code = input(">>> ")
                if user_code.lower() == "exit":
                    typewriter("Exiting compiler...")
                    break               
                try:
                    exec(user_code)
                except Exception as e:
                    print("Error:", e)
            os.system('cls')
        elif name == 'c':
            os.system('cls')
            typewriter("This is how printing text with numbers works in python")
            typewriter("INPUT:\n\tprint(\"My age is\", 18)\n\nOUTPUT:\n\tMy age is 18")
            time.sleep(2)
            input("\npress enter to try how to use print: ")
            os.system('cls')
            typewriter("Type \'exit\' if you want to leave.\n")
            time.sleep(2)
            while True:
                user_code = input(">>> ")
                if user_code.lower() == "exit":
                    typewriter("Exiting compiler...")
                    break               
                try:
                    exec(user_code)
                except Exception as e:
                    print("Error:", e)
            os.system('cls')
        elif name == 'x':
            os.system('cls')
            break
        else:
            print("Invalid Input!")

def variables():
    os.system('cls')
    print("EXPLANATION:")
    typewriter("\tA variable in Python is a name you create to store a value in your program. It works like a container")
    typewriter("\tor a box where you keep information that you want to use later.")
    time.sleep(1)
    typewriter("\tEXAMPLE:\n\t\tname = \'Mark\'\n\t\tage = 17")
    time.sleep(1)
    typewriter("\tyou are storing the words “Mark” and the number 17 inside variables. This makes your program more")
    typewriter("\tflexible because you can save data, change it, and reuse it anytime. Variables are important because")
    typewriter("\tthey help your program remember information, perform calculations, and interact with the user.")
    time.sleep(.5)
    typewriter("\nNow I will show you how to use variable using print")
    input("\npress enter to continue: ")
    typewriter("\nINPUT:\n\tname = \'Mark Andrei\'\n\n\tprint(\"My name is\", name)")
    typewriter("\nOUTPUT:\n\tMy name is Mark Andrei")
    input("\npress enter to try: ")
    os.system('cls')
    typewriter("Type \'exit\' if you want to leave.\n")
    time.sleep(2)
    storage = {}
    while True:
        trys = input(">>> ")
        if trys.lower() == "exit":
            typewriter("Exiting compiler...!")
            break   
        try:
            exec(trys, storage)
        except Exception as e:
            print("Error:", e)
    os.system('cls')
