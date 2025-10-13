loan = eval(input("Enter loan amount: "))
year = eval(input("Enter loan period in years: "))
months = year * 12
principal = loan / months
balance = loan
print("Months\t|Principal Payment\t |Remaining Balance\t|Interest\t\t|Monthly Payment")

for i in range(1, months+1, 1):
    balance -= principal
    interest = balance * 0.03
    monthly = principal + interest
    print(f"{i}\t|\t{round(principal,2)} \t\t |\t{round(balance,2)}\t\t|\t{round(interest,2)}\t\t|\t{round(monthly,2)}")