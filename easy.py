for i in range(1,6,1):
    for d in range(6,i,-1):
        print(" ", end=" ")
    for f in range(1,2*i,1):
        print("*", end=" ")
    print()

for i in range(1,6,1):
    for j in range(0,i,1):
        print(i, end=" ")
    print()