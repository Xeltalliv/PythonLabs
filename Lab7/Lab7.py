#!/usr/bin/env python
import random

print("Задача: Для заданого масиву дійсних чисел, серед яких є і відемні, знайти величину і індекс найменшого серед додатних\nчисел. Поміняти знайдений і максимальний елемент масиву.")
print("=" * 119)

# введення
arrayLen = int(input("Введіть розмір масива: "))
array = [random.randint(-50, 50) for _ in range(arrayLen)]
print("Масив: "+ str(array));
print("=" * 119)

# пошук потрібних наченнь
minValue = 0
minIndex = -1
maxValue = array[0]
maxIndex = 0
for i in range(len(array)):
	if (array[i] > 0 and (minIndex == -1 or array[i] < minValue)):
		minValue = array[i]
		minIndex = i
	if (array[i] > maxValue):
		maxValue = array[i]
		maxIndex = i

# обмін та виведення результату
if (minIndex == -1):
	print("Значень більше нуля немає")
else:
	print("Найменше  додатнє число: array["+str(minIndex)+"] = "+str(minValue))
	print("Найбільше додатнє число: array["+str(maxIndex)+"] = "+str(maxValue))
	print("Зміна їх місцями:")
	array[minIndex], array[maxIndex] = array[maxIndex], array[minIndex]
	print(str(array))