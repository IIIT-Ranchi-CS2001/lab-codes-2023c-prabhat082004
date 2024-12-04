s = "Ba Ba Black Sheep"
print(len(s))
for i in s:
    if i == 'e':
        print(s.index(i))
        break;

countA = 0
for i in s:
    if i == 'a':
        countA += 1
print(countA)

s3 = s.replace('B', 'T', 2)
print(s3)

