import os

os.system('clear')
print("======================================================\n===============This is a python compiler==============")
while True:
    print("======================================================")    
    choose = input("\tA. Start\n\tB. What is Python Compiler?\n\tC. Exit\nInput here ---> ").lower()
    if choose == 'a':
        os.system('clear')
        while True:
            learn = input("What do you want to learn? Choose below.\n\tA. Printing\n\tB. Conditional Statement\n\tC. For Loop\n\tD. String Formatting\n\tE. Parameter\n\tF. While Loop\n\tG. Basic List Operation\n\tX. Exit\nType here ---> ").lower()
            if learn == 'a':
                while True:
                    how = input("\tA. print\n\tB. input\n\tC. Back\nType here ---> ").lower()
                    if how == 'a':
                        print("OUTPUT:\n\tHello World\n")
                        while True:
                            wow = input("Input:\n\tprint(\"Hello World\")\n\n\tA. Explanation\n\tB. Back\nType here ---> ")
                            if wow == 'a':
                                print("EXPLANATION:\n\tIn Python, print() is a built-in function used to\n\tdisplay text or other data on the screen. When you\n\tcall print(), Python converts the value you provide\n\tinto a readable string (if it isn\'t already one) and\n\tsends it to the standard output, which is usually\n\tyour console or terminal. and always don\'t forget\n\tto use double comma(\"\") inside the parentheses")
                                print("============================================================")
                                break
                            else:
                                print("Invalid Input")
                                continue
                        continue
                    elif how == 'b':
                        examp = input("EXAMPLE OUTPUT:\n\tWhat is your name? ")
                        print(f"\tHello {examp}, It\'s nice to see you here.")
                        while True:
                            wow = input("\nInput:\n\tvariable = input(\"What is your name? \")\n\tprint(f\"Hello {variable}, It\'s nice to see you here.\")\n\n\tA. Explanation\n\tB. EVAL\n\tC. LEN\nType here ---> ")
                            if wow == 'a':
                                print("EXPLANATION:\n\tinput() is a built-in Python function used to receive\n\tinformation from the user while the program is running.\n\tIt is one of the main ways Python programs can interact\n\twith people in real time. When you use input(), your\n\tprogram pauses and waits until the user types something\n\tand presses Enter. After that, the function returns the\n\ttext the user typed.")
                                print("===============================================================")
                                continue
                            elif wow == 'b':
                                pass
                                break
                            elif wow == 'c':
                                pass
                                break
                            else:
                                print("Invalid Input")
                                continue
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
