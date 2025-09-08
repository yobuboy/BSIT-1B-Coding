temp = eval(input("Enter temperature ---> "))

if temp <= 0:
	print("Temperature is considered as BELOW FREEZING")
elif temp <= 15:
	print("Temperature is considered as EXTREMELY COLD")
elif temp <= 30:
	print("Temperature is considered as COLD")
elif temp <= 38:
	print("Temperature is considered as LUKEWARM")
elif temp <= 42:
	print("Temperature is considered as WARM")
elif temp <= 50:
	print("Temperature is considered as HOT")
elif temp <= 60:
	print("Temperature is considered as EXTREMELY HOT")
elif temp >= 61:
	print("Temperature is considered as BURNING TEMPERATURE")
else:
	print("Invalid Temperature")
