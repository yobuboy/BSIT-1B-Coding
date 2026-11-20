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

https://www.figma.com/design/WaAw51ePCa76AhmP3Y92pG/webd?node-id=12-46&t=BmA7l8oLOcVsxBtO-1&fbclid=IwY2xjawVs-qVleHRuA2FlbQIxMQBwZG9mBXNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABH9Bod8yYye4l_o9tjvdsa-7ubj8VFKQZZ6kvw-1xNwWl4ZUu0QO9cZO-QY25_aem_Ra9KvBEZcbPshwhDcDh8Ng