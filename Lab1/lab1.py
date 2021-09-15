import math

height = float(input("Введіть висоту фігур: "))
radius = float(input("Введіть радіус фігур: "))

cillinderVolume = radius * math.pi * height
coneVolume = 1 / 3 * math.pi * radius * radius * height

print("Об'ем циліндра: "+str(cillinderVolume))
print("Об'ем конуса: "+str(coneVolume))
