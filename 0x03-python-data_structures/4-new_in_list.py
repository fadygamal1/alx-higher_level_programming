#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''replaces an element in a list at a specific position
       without modifying the original list
       Args:
            :my_list -  original list
            :idx - index of element to be replaced
            :element - value of the element
       Return:
            :a new list
    '''
    if idx < 0 or idx > (len(my_list)) - 1:
        return my_list

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
