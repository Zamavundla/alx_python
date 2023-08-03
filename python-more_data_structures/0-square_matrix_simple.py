def square_matrix_simple(matrix=[]):
    # Create an empty result matrix with the same size as the input matrix
    result_matrix = [[0 for _ in row] for row in matrix]

    # Compute the square value of each element and store it in the result matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

#matrix1 = [[1, 2], [3, 4]]
#print(square_matrix_simple(matrix1))
# Output: [[1, 4], [9, 16]]

#matrix2 = [[0, -1], [2, 3]]
#print(square_matrix_simple(matrix2))
# Output: [[0, 1], [4, 9]]
