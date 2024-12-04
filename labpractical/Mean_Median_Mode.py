from collections import Counter
list = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list.append(element)
sort_list = sorted(list)
mean = (sum(sort_list))/n
print("Mean of the list is",mean)  
if n % 2 == 1:
        median = sort_list[n // 2]
else:
     middle1 = sort_list[n // 2]
     middle2 = sort_list[n // 2 - 1]
     median = (middle1 + middle2) / 2
print("Median of the list is",median) 
count = Counter(list)
max_count = max(count.values())
mode = [key for key, value in count.items() if value == max_count]
print("Mode of the list is",mode)