import random

number = random.randint(-10000, 10000)
last_digit = number % 10  # Get the last digit

message = "Last digit of {}, followed by\nthe number, followed by\nthe string is {}, followed by".format(number, last_digit)

if last_digit > 5:
    message += " the string and is greater than 5"
elif last_digit == 0:
    message += " the string and is 0"
else:
    message += " the string and is less than 6 and not 0"

print(message)
