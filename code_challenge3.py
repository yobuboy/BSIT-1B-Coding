name = input("What is your name? --> ")
fare = eval(input("Magkano bayad mo? --> "))
tao = input("Are you a student? (yes or no) ")

if tao.lower() == 'yes' :
    percent = fare * .2
    bayad = fare - percent
    print(name, "You are eligible to a student discount \nThis is your discount:", percent ,"\nHere's the total amount:", bayad)
else:
    print(name,"Sorry, you can't get a fare discount")
