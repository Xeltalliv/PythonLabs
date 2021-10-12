#!/usr/bin/env python

print("Задача: Знайти cos(x) з точністю eps")
x = float(input("Введіть x: "))
eps = float(input("Введіть eps: "))

add = 1
summ = 0
i = 0

while abs(add) > eps:
	i += 2
	summ += add
	print("Додано "+str(add))
	add *= (-x*x) / ((i-1)*i)

print("======================");
print("Резуьтат: "+str(summ))