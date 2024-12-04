customer_names = [f"Customer{i}" for i in range(1, 6)]
customer_ids = [1000 + i for i in range(1, 6)]
shopping_points = [10 * i for i in range(1, 6)]
customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))
customer_data_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
print("Using zip():", customer_data_zip)
print("Without using zip():", customer_data_manual)