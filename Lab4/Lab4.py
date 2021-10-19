#!/usr/bin/env python

print("Задача: Обчислити 1 - 1/2 + 1/3 - 1/4 +1/5 ... + 1/99 - 1/100 послідовно зліва направо і навпаки, результати порівняти.")
print("=" * 119)

sum1 = 0
sign = 1
for add in range(1, 101, 1):
	sum1 += sign / add
	sign = 0 - sign

sum2 = 0
sign = 1
for add in range(100, 0, -1):
	sum2 += sign / add
	sign = 0 - sign

print("1 - 1/2 + 1/3 - 1/4 + 1/5  ... + 1/99 - 1/100 = " + str(sum1))
print("1/100 - 1/99 + 1/98 - 1/97 ... + 1/2  - 1     = " + str(sum2))