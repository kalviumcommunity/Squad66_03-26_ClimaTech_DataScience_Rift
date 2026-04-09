# Passing Data into Functions and Returning Results

# -----------------------
# Function with parameters and return
# -----------------------
def calculate_sum(a, b):
    return a + b

# Call function and store result
result = calculate_sum(10, 20)
print("Sum:", result)


# -----------------------
# Using returned value in further computation
# -----------------------
def square(num):
    return num * num

value = square(result)
print("Square of sum:", value)


# -----------------------
# Function with multiple operations
# -----------------------
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

data = [10, 20, 30, 40]
avg = calculate_average(data)
print("Average:", avg)


# -----------------------
# Avoiding hardcoding (flexible function)
# -----------------------
def greet(name):
    return "Hello " + name

message = greet("Sreedhil")
print(message)