def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                # Last element in the row without space after it
                print("{:d}".format(row[i]), end="")
            else:
                # Elements in the row with space after each element
                print("{:d}".format(row[i]), end=" ")
        print()  # Move to the next line after printing each row


#matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print_matrix_integer(matrix1)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

#matrix2 = [[10, 20], [30, 40, 50], [60]]
#print_matrix_integer(matrix2)
# Output:
# 10 20
# 30 40 50
# 60

#matrix3 = [[]]
#print_matrix_integer(matrix3)
# Output: (empty line)
