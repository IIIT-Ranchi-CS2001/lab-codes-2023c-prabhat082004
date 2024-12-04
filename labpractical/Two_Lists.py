name = [input("Enter name: ").split()]
age = [int(input("Enter age: ")).split()]
gender = [input("Enter gender: ").split()]
income = [int(input("Enter income: ").split())]
l=len(name)
for i in range(l):
    l.append(name[i]+":"+age[i]+":"+gender[i]+":"+income[i])
print(l)