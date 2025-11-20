# this program gives a diamond output
for drei in range(1,11,1):
    for h in range(10, drei, -1):
        print(" ", end=" ")
    for g in range(1, drei, 1):
        print("x", end=" ")
    for i in range(1, drei,1):
        print("x", end=" ")
    print()

for drei in range(1,11,1):
    for h in range(1, drei, 1):
        print(" ", end=" ")
    for g in range(10, drei, -1):
        print("x", end=" ")
    for i in range(10, drei,-1):
        print("x", end=" ")
    print()
