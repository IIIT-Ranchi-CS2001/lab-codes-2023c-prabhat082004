n = input("Enter the string: ")
c = input("Enter the character to count: ")
count = 0
for char in n:
    if char == c:
        count+=1
print("The character",c,"occurs",count,"times in the string.")