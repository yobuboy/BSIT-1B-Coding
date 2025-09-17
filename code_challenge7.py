count = eval(input("COUNTDOWN TIMER SIMULATOR\nEnter the starting number for countdown: "))
print("Countdown started:")
import time
for s in range(count, 0, -1):
    print(s)
    time.sleep(1)
print("Liftoff!")