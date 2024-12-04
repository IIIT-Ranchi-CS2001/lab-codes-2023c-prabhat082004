string = input("Enter any string: ")
size = len(string)
if string[:size] == string[size::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")