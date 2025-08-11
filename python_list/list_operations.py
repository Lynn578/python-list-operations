# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append:", my_list)  # [10, 20, 30, 40]

# Insert 15 at the second position
my_list.insert(1, 15)
print("After insert:", my_list)  # [10, 15, 20, 30, 40]

# Extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extend:", my_list)  # [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element
my_list.pop()
print("After pop:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# Sort the list
my_list.sort()
print("After sort:", my_list)  # [10, 15, 20, 30, 40, 50, 60]

# Find the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)  # Output: 3
print("Final list:", my_list)  # [10, 15, 20, 30, 40, 50, 60]