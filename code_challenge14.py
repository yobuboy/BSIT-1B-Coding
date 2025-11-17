import os

os.system('cls')

print('STUDENT INFORMATION SYSTEM')
print("=======================================")

# Empty dictionary
student_record = {}

while True:
    print("SELECT FOR THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - EXIT SYSTEM")
    print("=========================================")
    choice = input("SELECT FROM THE OPTIONS ABOVE ---> ").lower()

    if choice == 'a':
        os.system('cls')
        print("\nADDING STUDENT RECORD")
        id_no = input("Please input student ID number ---> ")
        first_name = input("Please input student First Name ---> ").upper()
        second_name = input("Please input student Second Name ---> ").upper()
        last_name = input("Please input student Last Name ---> ").upper()
        age = eval(input("Input student age ---> "))
        course = input("Input student Course ---> ").upper()
        section = input("Input student Section ---> ").upper()

        student_record[id_no] = [first_name,second_name,last_name, age, course,section]
        print("DATA SAVED SUCCESSFULLY")
        # Go back to the original menu
        continue
    elif choice == 'b':
        os.system('cls')
        for i, j in student_record.items():
            print(f"STUDENT ID - {i}    |INFORMATION - {j}")
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        break
    else:
        print("INVALID CHOICE")
        continue