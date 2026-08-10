import math
import random
import datetime

# 1. Math module - Square root
number = float(input("Enter a number to find its square root: "))

if number >= 0:
    square_root = math.sqrt(number)
    print("Square root of", number, "=", square_root)
else:
    print("Square root cannot be calculated for a negative number.")

# 2. Random module - Generate random number
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# 3. Datetime module - Current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)
