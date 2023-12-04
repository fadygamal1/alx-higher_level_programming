#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    ''' prints a matrix of integers
        :Args:
            matrix of integers = nested list
        :Return:
            None
    '''
    for row_id in range(0, len(matrix)):  # for each row in matrix
        sep = ' '
        for col_id in range(0, len(matrix[row_id])):  # for each int in row
            if col_id == len(matrix[row_id]) - 1:  # end of row
                sep = ''
            print("{:d}".format(matrix[row_id][col_id]), end=sep)

        print('')
