# Writing Conditional Statements in Python

# -----------------------
# Basic if statement
# -----------------------
num = 10

if num > 5:
    print("Number is greater than 5")


# -----------------------
# if-else statement
# -----------------------
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# -----------------------
# if-elif-else statement
# -----------------------
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


# -----------------------
# Logical operators
# -----------------------
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("Good weather for outdoor activities")

if temperature > 35 or is_raining:
    print("Stay indoors")