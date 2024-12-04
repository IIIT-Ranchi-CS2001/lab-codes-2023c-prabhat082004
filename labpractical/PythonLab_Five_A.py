def my_zip(list1, list2, list3, check):
    customer_details = []
    if(strct):
        for i in range(len(list1)):
            customer_details.append((list1[i], list2[i], list3[i]))
        return customer_details
    min_length = min(len(list1), len(list2), len(list3))
    for i in range(min_length):
        customer_details.append((list1[i], list2[i], list3[i]))
    return customer_details

list_name = [n for n in input("Enter the names of customer: ").split()]
list_id = [int(n) for n in input("Enter the id of customer: ").split()]
list_shopping_points = [int(n) for n in input("Enter the shopping points of customer: ").split()]

list_name_size = len(list_name)
list_id_size = len(list_id)
list_shopping_points_size = len(list_shopping_points)

strct = (list_name_size == list_id_size and list_id_size == list_shopping_points_size) if True else False
print(my_zip(list_name, list_id, list_shopping_points, strct))