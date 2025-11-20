import random
import os
os.system('cls')

print('*****************************************************')
print('******************* GUESSING GAME *******************')
print('*****************************************************\n')

random_value = random.randint(0,10)
tries = 0
tuloy = True

while tuloy == True:
    r = eval(input(' guess a random number from 0 to 10 ---> '))

    tries += 1
    if r == random_value:
       print('NICE, you got it right!!')
       print(f'random value is {random_value}')
       break
    else:
        print('HAHAHA NOOB, you\'re wrong!!')
    continue
print(f'you guessed {tries} times')
