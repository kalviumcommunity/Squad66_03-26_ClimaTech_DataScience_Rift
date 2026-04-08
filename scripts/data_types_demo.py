# Understanding Numeric and String Data Types

# Numeric Data Types
a = 10          # integer
b = 3.5         # float

print("Integer value:", a)
print("Float value:", b)

# Arithmetic Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# String Data Types
name = "Rift"
message = "Welcome to Data Science"

print("Name:", name)
print("Message:", message)

# String Concatenation
full_message = name + " - " + message
print("Concatenated String:", full_message)

# Mixing Types (Conversion)
num = 25
text = "The number is "

# Correct way using conversion
print(text + str(num))

# Type Checking
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of name:", type(name))