def divide_numbers():
	try:
		number = int(input("Vvedite:"))
		result = 10 / number
		print("Результат деления: ",result)
	except ZeroDivisionError:
		print("Error zerodev")
	except ValueError:
		print("Error")
	print("Vse ok")

divide_numbers()