import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # Get the last digit

message = "Last digit of {}\nis {}\nand is".format(number, last_digit)

if last_digit == 0:
    message += " 0"
elif last_digit > 5:
    message += " greater than 5"
else:
    message += " less than 6 and not 0"

print(message)
