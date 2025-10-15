bake = True
while bake == True:
    num = input("Do you still want to bake a cake? [yes/no] ").lower()
    if num == 'yes':
        print("Your cake is cooking.....")
        continue
    else:
        print("your cake is done!!")
        break