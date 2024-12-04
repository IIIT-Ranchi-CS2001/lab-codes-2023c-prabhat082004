s1 = "Maha Bharat"
print(s1[0].lower() + s1[1:5].upper() + s1[5].lower() + s1[6:11].upper())
print(s1[5:11])
print(s1[5:11] * 3)
s2 = s1.replace(s1[0:4], "Mera")
print(s2)
print(s2 + " Mahan")