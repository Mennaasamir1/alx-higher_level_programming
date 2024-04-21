#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 10:
	Last_digit = number % 10
else:
	Last_digit = number % -10
print(f"Last digit of {number} is {Last_digit}")

if Last_digit > 5:
	print(f"and is greater than 5")
elif Last_digit == 0:
	print(f"and is 0")
else:
	print(f"and is less than 6 and not 0")	
