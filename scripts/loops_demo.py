# Using for and while Loops in Python

# -----------------------
# for loop (range)
# -----------------------
print("For loop with range:")
for i in range(1, 6):
    print(i)


# -----------------------
# for loop (list)
# -----------------------
numbers = [10, 20, 30]

print("\nFor loop with list:")
for num in numbers:
    print(num)


# -----------------------
# while loop
# -----------------------
print("\nWhile loop:")
count = 1

while count <= 5:
    print(count)
    count += 1  # important to avoid infinite loop


# -----------------------
# break example
# -----------------------
print("\nBreak example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# -----------------------
# continue example
# -----------------------
print("\nContinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)