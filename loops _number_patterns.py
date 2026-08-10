# Task 2: Loops and Number Patterns

n = int(input("Enter a number N: "))

# Print numbers from 1 to N using for loop
print("\nNumbers from 1 to", n, "using for loop:")

for i in range(1, n + 1):
    print(i, end=" ")

# Print numbers from N to 1 using while loop
print("\n\nNumbers from", n, "to 1 using while loop:")

i = n
while i >= 1:
    print(i, end=" ")
    i -= 1

# Multiplication table
print("\n\nMultiplication Table of", n)

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
