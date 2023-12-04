#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    ''' deletes the item at a specific position in a list.
        :Args:
            @my_list: list of integers
            @idx: index of element to delete

        :Return: a new list with element at idx removed
    '''
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    del my_list[idx]
    return my_list
