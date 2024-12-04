#Write a program to find:
#1) Area and Perimeter of a triangle 
#2) Find all angles of that triangle

import math
 
sideOne = int(input("Enter the first side of triangle: "))
sideTwo = int(input("Enter the second side of triangle: "))
sideThree = int(input("Enter the third side of triangle: "))

Perimeter = sideOne + sideTwo + sideThree
print("Perimeter of the triangle: ", Perimeter)

s = (Perimeter / 2)
Area = (s * (s - sideOne) * (s - sideTwo) * (s - sideThree)) ** 0.5
print("Area of the triangle: ", Area, "\n")

#Cosine formula
angleOne = math.acos(((sideTwo ** 2 + sideThree ** 2) - sideOne ** 2) / (2 * sideTwo * sideThree))
angleSecond = math.acos(((sideOne ** 2 + sideThree ** 2) - sideTwo ** 2 ) / (2 * sideOne * sideThree))
angleThree = math.acos(((sideOne ** 2 + sideTwo ** 2) - sideThree ** 2 ) / (2 * sideOne * sideTwo))

print("First Angle of the triangle: ", math.degrees(angleOne))
print("Second Angle of the triangle: ", math.degrees(angleSecond))
print("Third Angle of the triangle: ", math.degrees(angleThree))