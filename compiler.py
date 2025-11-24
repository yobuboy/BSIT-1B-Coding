import os

os.system('clear')
print("===============================================\n===============This is a python compiler============")
while True:
    print("===============================================")    
    choose = input("\tA. Start\n\tB. What is Python Compiler?\n\tC. Exit\nInput here ---> ").lower()
    if choose == 'a':
        os.system('clear')
        while True:
            learn = input("What do you want to learn? Choose below.\n\tA. Printing\n\tB. Conditional Statement\n\tC. For Loop\n\tD. String Formatting\n\tE. Parameter\n\tF. While Loop\n\tG. Basic List Operation\n\tX. Exit\nType here ---> ").lower()
            if learn == 'a':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'b':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'c':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'd':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'e':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'f':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'g':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back").lower()
                    if how == 'a':
                        pass
                        continue
                    elif how == 'b':
                        pass
                        continue
                    elif how == 'c':
                        pass
                        break
                    else:
                        print("Invalid Input")
                continue
            elif learn == 'x':
                pass
                break
            else:
                print("Invalid Input")
        continue
    elif choose == 'b':
        os.system('clear')
        print("A Python compiler is a program that reads Python code and helps beginners or non-programmers understand how the code works by converting it into a form the computer can run.")
        continue
    elif choose == 'c':
        os.system('clear')
        print("Thank you for your visit!")
        break
    else:
        os.system('clear')
        print("Invalit Input") 
        continue
