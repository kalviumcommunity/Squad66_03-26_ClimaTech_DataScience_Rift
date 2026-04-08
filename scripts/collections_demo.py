# Working with Lists, Tuples, and Dictionaries

# -----------------------
# LIST (mutable)
# -----------------------
numbers = [10, 20, 30, 40]

print("List:", numbers)

# Access element
print("First element:", numbers[0])

# Modify element
numbers[1] = 25
print("Modified list:", numbers)

# Add element
numbers.append(50)
print("After append:", numbers)

# Remove element
numbers.remove(30)
print("After removal:", numbers)


# -----------------------
# TUPLE (immutable)
# -----------------------
coordinates = (10, 20)

print("\nTuple:", coordinates)

# Access element
print("X coordinate:", coordinates[0])

# Trying to modify (will cause error if uncommented)
# coordinates[0] = 15


# -----------------------
# DICTIONARY (key-value)
# -----------------------
student = {
    "name": "Sreedhil",
    "age": 20,
    "course": "Data Science"
}

print("\nDictionary:", student)

# Access value
print("Name:", student["name"])

# Modify value
student["age"] = 21
print("Updated age:", student)

# Add new key
student["grade"] = "A"
print("After adding grade:", student)