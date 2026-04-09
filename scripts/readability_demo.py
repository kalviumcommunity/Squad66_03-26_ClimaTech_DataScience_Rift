# Demonstrating Readable Variable Names and Comments (PEP 8 Basics)

# Bad example (unclear variable names)
a = 10
b = 20
c = a + b
print(c)


# Good example (clear and descriptive variable names)
first_number = 10
second_number = 20
total_sum = first_number + second_number

print("Total Sum:", total_sum)


# Function with meaningful naming and comments
def calculate_average(numbers_list):
    # Calculate the average of a list of numbers
    total = sum(numbers_list)
    count = len(numbers_list)
    return total / count


# Using the function
sample_data = [10, 20, 30, 40]
average_value = calculate_average(sample_data)

print("Average:", average_value)


# Example of meaningful comment
temperature_celsius = 30

# Convert Celsius to Fahrenheit for display
temperature_fahrenheit = (temperature_celsius * 9/5) + 32

print("Temperature in Fahrenheit:", temperature_fahrenheit)