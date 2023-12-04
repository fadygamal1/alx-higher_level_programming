#!/usr/bin/python3

def max_integer(my_list=[]):
    ''' finds the biggest integer of a list.
        :Args:
            @my_list: list of integers
        :Return: maximum value in @my_list
    '''
    if len(my_list) == 0:
        return None

    maximum_int = my_list[0]
    for num in my_list:
        if num > maximum_int:
            maximum_int = num

    return maximum_int
