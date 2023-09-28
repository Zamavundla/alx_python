#printing a combination of two digits from 00 to 99
for i in range(0, 100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
    