#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() not in ('c', 'C'):
            result += char
    return result

#print(no_c("Hello World"))  # Output: "Hello World"
#print(no_c("Python is Cool"))  # Output: "Python is ool"
#print(no_c("Can you see C's?"))  # Output: "an you see 's?"
