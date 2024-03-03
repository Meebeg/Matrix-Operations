

# #1st Task
# import random as rd
# def generate_random_matrix(rows, cols):
#     matrix = []
#     for _ in range(rows):
#         row = [rd.randint(1, 100) for _ in range(cols)]
#         matrix.append(row)
#     return matrix


# rd_mat = generate_random_matrix(2, 4)
# for row in rd_mat:
#     print(row)

# #2nd Task
# def get_column_sum(matrix, index):
#     col_sum= 0
#     for row in matrix:
#         col_sum += row[index]
#     return col_sum
# matrix = [
#     [5, 6 ,8],
#     [4, 5 ,6]
#     ]
# index = 0
# col_sum = get_column_sum(matrix, index)
# print(matrix, "The sum of column", index, "is:", col_sum)

def get_row_average(matrix, index):
    row_values = matrix[index]
    row_average = sum(row_values) / len(row_values)
    return row_average
matrix = [
    [5, 6 ,8],
    [4, 5 ,6]
    ]
index = 0
row_average = get_row_average(matrix, index)
print(matrix, "The average of rows", index, "is:", row_average)
