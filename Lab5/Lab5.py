#!/usr/bin/env python

print("Задача: Знайти цифрові корені всіх простих чисел з інтервалу [100, 200]")
print("=" * 119)

for iterator in range(100, 201, 1):
	number = iterator
	string = str(number) + " --> "
	while number >= 10:
		newNumber = 0
		localString = ""
		while number >= 10:
			digit = number % 10
			newNumber += digit
			localString = " + " + str(digit) + localString
			number = number // 10
		newNumber += number
		string += str(number) + localString + " --> "
		number = newNumber
	print(string + str(number))