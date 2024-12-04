import math
user_input = input("Enter the first coordinates in space seperated by commas: ")
point1 = tuple(map(int, user_input.split(',')))
User_input = input("Enter the second coordinates in space seperated by commas: ")
point2 = tuple(map(int, User_input.split(',')))
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
print(f"Euclidean distance between the two points: {distance}")