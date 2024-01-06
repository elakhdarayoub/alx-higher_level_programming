#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(0, len(row)):
            if element < len(row) - 1:
                print("{:d} ".format(row[element]), end='')
            else:
                print("{:d}".format(row[element]), end='')
        print()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
