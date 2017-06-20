# FizzBuzz

def fizzbuzz():
	checknum=3


	if checknum%5==0 and checknum%3==0:
		print("FizzBuzz")

	elif checknum%5==0:
		print("Buzz")
	elif checknum%3==0:
		print("Fizz")
	
	else:
		print(checknum)



fizzbuzz()

