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
                        while True:
                            wow = input("OUTPUT:\n\tHello World\n\nInput:\n\tprint(\"Hello World\")\n\n\tA. Explanation\n\tB. Back\nType here ---> ")
                            if wow == 'a':
                                print("EXPLANATION:\n\tIn Python, print() is a built-in function used to\n\tdisplay text or other data on the screen. When you\n\tcall print(), Python converts the value you provide\n\tinto a readable string (if it isn\'t already one) and\n\tsends it to the standard output, which is usually\n\tyour console or terminal. and always don\'t forget\n\tto use double comma(\"\") inside the parentheses")
                                continue
                            elif wow == 'b':
                                pass
                                break
                            else:
                                print("Invalid Input")
                                continue
                        continue
                    elif how == 'b':
                        examp = input("EXAMPLE OUTPUT:\n\tWhat is your name?\nType here ---> ")
                        print(f"Hello {examp}, It\'s nice to see you here.")
                        wow = input("\nInput:\n\tprint(\"Hello World\")\n\n\tA. Explanation\n\tB. EVAL\n\tC. LEN\nType here ---> ")
                        while True:
                            if wow == 'a':
                                print("EXPLANATION:\n\tIn Python, print() is a built-in function used to\n\tdisplay text or other data on the screen. When you\n\tcall print(), Python converts the value you provide\n\tinto a readable string (if it isn\'t already one) and\n\tsends it to the standard output, which is usually\n\tyour console or terminal. and always don\'t forget\n\tto use double comma(\"\") inside the parentheses")
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
