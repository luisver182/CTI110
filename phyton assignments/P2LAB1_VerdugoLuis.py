# Verdugo Luis
# 04/21/2025
# P2LAB1
# circle math calculations

import math
radius = float(input("What is the radius of the circle: "))
diameter = 2 * radius
circumference = 2 * 3.1416 * radius
area = math.pi * (radius ** 2)
print(f'The diameter of the circle is:{diameter: .1f}')
print(f"The circunference of the circle is: {circumference: .2f}")
print(f"The area of the circle is: {area: .3f}")
