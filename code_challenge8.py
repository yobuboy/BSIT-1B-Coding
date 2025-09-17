number = eval(input("MULTIPLICATION TABLE MAKER\nEnter a number: "))
print("Multiplication table for",number,":")
for s in range(1, 11, 1):
    print(number,"x",s,"=",number * s)