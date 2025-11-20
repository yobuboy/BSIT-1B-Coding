fname = 'Mark Andrei'
mname = 'Jaca'
lname = 'Alba'
print(f"My full name is {fname} {mname} {lname}")

fname = 'Mark Andrei'
mname = 'Jaca'
lname = 'Alba'
print(f"My full name is {fname.upper()} {mname.upper()} {lname.upper()}")

sum = 0 
for i in range(1, 6):
    x  = eval(input(f"{i} - Input a number --> "))
    sum += x 
print(f"The total sum is {sum}")
# string formating is use to make your program looks clean and lessen the use of comma that leads to an error when you forgot to add comma every variable that you add.
