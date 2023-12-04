#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ''' adds 2 tuples.
        Args:
            :tuples of integers
        Return:
            : tuple where each element is the sum of
            the identical elements in same position in tuple @a, and @b
        :Return: tuple with two elements
    '''
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    sum_of_first_index = sum_of_second_index = 0

    if len_a >= 1:
        sum_of_first_index = tuple_a[0]
    if len_a > 1:
        sum_of_second_index = tuple_a[1]

    if len_b >= 1:
        sum_of_first_index += tuple_b[0]
    if len_b > 1:
        sum_of_second_index += tuple_b[1]

    return (sum_of_first_index, sum_of_second_index)
