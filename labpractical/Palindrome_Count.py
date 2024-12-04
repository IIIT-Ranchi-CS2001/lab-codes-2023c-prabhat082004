a = input("Enter a sentence: ")
b = a.split()
count = sum(word.lower() == word.lower()[::-1] for word in b)
print("Number of palindrome words:",count)