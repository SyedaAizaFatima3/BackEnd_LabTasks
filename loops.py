
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)



# range(5) gives numbers from 0 to 4
for i in range(5):
    print(i)

# range(start, stop)
# 1 to 5
for i in range(1, 6):
    print(i)

# range(start, stop, step)
# Even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

# Reverse numbers from 5 to 1
for i in range(5, 0, -1):
    print(i)

name = "Python"

# Loop through every character
for letter in name:
    print(letter)

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


i = 1

while i <= 5:
    print(i)

    # Increase i by 1
    # Without this, the loop may become infinite
    i += 1

i = 5

while i >= 1:
    print(i)

    # Decrease i by 1
    i -= 1


for i in range(1, 11):

    # % gives remainder
    # If remainder is 0, number is even
    if i % 2 == 0:
        print(i, "is Even")

    else:
        print(i, "is Odd")

total = 0

for i in range(1, 11):

    # Add each number to total
    total += i

print("Sum =", total)


num = 5

for i in range(1, 11):

    print(num, "x", i, "=", num * i)


# break completely stops the loop

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# continue skips the current iteration

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# pass does nothing
# It is used as a placeholder

for i in range(1, 6):

    if i == 3:
        pass

    print(i)


# A loop inside another loop

for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)


for i in range(1, 6):

    print("Table of", i)

    for j in range(1, 11):

        print(i, "x", j, "=", i * j)

    print()


# Output:
# *
# **
# ***
# ****
# *****

for i in range(1, 6):

    print("*" * i)


for num in range(2, 51):

    is_prime = True

    for i in range(2, num):

        if num % i == 0:

            is_prime = False
            break

    if is_prime:
        print(num)


# ============================================================
# 25. FACTORIAL
# ============================================================

# Example:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = 5

factorial = 1

for i in range(1, num + 1):

    factorial *= i

print("Factorial =", factorial)


# ============================================================
# 26. REVERSE A NUMBER
# ============================================================

num = 12345

reverse = 0

while num > 0:

    # Get last digit
    digit = num % 10

    # Add digit to reverse
    reverse = reverse * 10 + digit

    # Remove last digit
    num //= 10

print("Reverse =", reverse)


num = 12345

count = 0

while num > 0:

    # Remove last digit
    num //= 10

    count += 1

print("Number of digits =", count)

