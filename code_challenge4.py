anime = input("Welcome to the world of manga\nI can recommend a manga's that based on your genre\nPlease choose a genre: (Action, Comedy, Romance); ").lower()
if anime == 'action':
    man1 = input("How long should the manga be? (Short, Medium, Long): ").lower()
    if man1 == 'short':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'All you need is Kill'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Bakuman'. ")
        else:
            print("The recommendation cannot be proccessed!")
    elif man1 == 'medium':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Dorohedoro'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Alice in Borderland'. ")
        else:
            print("The recommendation cannot be proccessed!")
    elif man1 == 'long':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'One Piece'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Attack on Titan'. ")
        else:
            print("The recommendation cannot be proccessed!")
    else:
        print("The recommendation cannot be proccessed!")
elif anime == 'comedy':
    man1 = input("How long should the manga be? (Short, Medium, Long): ").lower()
    if man1 == 'short':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Beck'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Saint Young Men'. ")
        else:
            print("The recommendation cannot be proccessed!")
    elif man1 == 'medium':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Astro Boy'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Arakwwa Under the Bridge'. ")
        else:
            print("The recommendation cannot be proccessed!")
    elif man1 == 'long':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Gintama'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Hinamatsuri'. ")
        else:
            print("The recommendation cannot be proccessed!")
    else:
        print("The recommendation cannot be proccessed!")
elif anime == 'romance':
    man1 = input("How long should the manga be? (Short, Medium, Long): ").lower()
    if man1 == 'short':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Millennium Snow'. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Dengeki Daisy'. ")
        else:
            print("The recommendation cannot be proccessed!")
    elif man1 == 'medium':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Eyes' by Katra Masaku. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Kimi ni Todoke: From me to You'. ")
        else:
            print("The recommendation cannot be proccessed!")
    elif man1 == 'long':
        den = input("Which decade? (2000s, 2010s): ").lower()
        if den == '2000':
            print("I highly recommended the manga called 'Skip Beat!' by Yoshiki Nakamura. ")
        elif den == '2010':
            print("I highly recommended the manga called 'Ao Haru Ride'. ")
        else:
            print("The recommendation cannot be proccessed!")
    else:
        print("The recommendation cannot be proccessed!")
else:
    print("The recommendation cannot be proccessed!")