#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ''' finds all multiples of 2 in a list.
        :Args:
            @my_list: list of integers
        :Return: boolean values for multiples of two
    '''
    return [num % 2 == 0 for num in my_list]
