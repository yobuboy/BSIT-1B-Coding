print("Welcome to the ODD Number Summation!")
num = 0
for a in range(1, 8, 1):
    den = eval(input("Enter random number:"))
    if den % 2 == 1:
        num += den
print("The summation of all add number is", num)