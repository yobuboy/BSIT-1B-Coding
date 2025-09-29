#start - optional value / parameter - default 0
#stop - required parameter / value
#step - optional value / parameter - default 1

for yes in range(1,11,1):
    for man in range(1,yes,1):
        print(f"M", end=" ")
    for you in range(10, yes,-1):
        print(f"W", end=" ")
    print()