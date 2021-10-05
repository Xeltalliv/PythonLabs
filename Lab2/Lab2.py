#!/usr/bin/env python

a = float(input("Введіть A: "))
b = float(input("Введіть B: "))
c = float(input("Введіть C: "))

if (a+b)%2 == 0:
	res = True
elif (b+c)%2 == 0:
	res = True
elif (a+c)%2 == 0:
	res = True
else:
	res = False

print("Є" if res else "Немає")
