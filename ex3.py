def fizzBuzz():
	fizzBuzzNum=False
	# isinstance(checknum, int)

	while not fizzBuzzNum:
		checkNum=int(input("Input No:").strip())
		
		divisibleby5=(checkNum%5==0)
		divisibleby3=(checkNum%3==0)

		if divisibleby5 and divisibleby3:
			print("FizzBuzz")
			fizzBuzzNum=True
		elif divisibleby5:
			print("Buzz")
			fizzBuzzNum=True
		elif divisibleby3:
			print("Fizz")
			fizzBuzzNum=True
		else:
			print("Not FizzBuzz Numner")


fizzBuzz()