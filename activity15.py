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