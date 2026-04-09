# Defining and Calling Python Functions

# -----------------------
# Simple function
# -----------------------
def greet():
    print("Hello, welcome to Data Science!")

# Call the function
greet()


# -----------------------
# Function with parameters
# -----------------------
def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

# Call function with arguments
add_numbers(10, 20)


# -----------------------
# Function with return value
# -----------------------
def multiply(x, y):
    return x * y

result = multiply(5, 4)
print("Multiplication result:", result)


# -----------------------
# Function demonstrating scope
# -----------------------
def show_number():
    num = 100   # local variable
    print("Inside function:", num)

show_number()

# Global variable
num = 50
print("Outside function:", num)