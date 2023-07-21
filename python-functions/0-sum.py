def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
