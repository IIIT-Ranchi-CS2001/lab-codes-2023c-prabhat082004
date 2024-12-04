import math
user_input = input("Enter the first coordinates in space seperated by commas: ")
point1 = tuple(map(float, user_input.split(',')))
User_input = input("Enter the second coordinates in space seperated by commas: ")
point2 = tuple(map(float, User_input.split(',')))
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
p = ((point1[0]-point2[0])/(point1[1]-point2[1]))
q = p*point1[1]
r = point1[0]-q
print(f"x - {p}y = {r}")