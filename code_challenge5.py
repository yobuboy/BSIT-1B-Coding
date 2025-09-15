print("Welcome to the Factor Program!")
num = 1
den = eval(input("Enter number:"))
for a in range(den, 0, -1):
    num *= a
print("The Factor is ", num)
