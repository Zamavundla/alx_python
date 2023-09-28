#printing all possible combinations of two digits 0 and 1 are considered same combination
def comb3():
    for i in range(0, 9):
        for j in range(i+1, 10):
            if i != j:
                print("{:d}{:d}".format(i, j), end=", " if i < 8 else "\n")
comb3()