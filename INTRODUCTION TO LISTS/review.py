# How to create List:
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]

# How to access, add, remove, and modify list elements
preferred_size.append("Medium")
print(preferred_size)

# How to create a two-dimensional list
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False
print(customer_data)
customer_data[1].remove(False)
print(customer_data)

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

