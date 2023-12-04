#!/usr/bin/python3

def no_c(my_string):
    '''removes all characters c and C from a string.
       Args:
            :my_string -  original string
       Return:
            :the new string
    '''
    new_string = ''
    for i in range(0, len(my_string)):
        if my_string[i] in 'cC':
            continue

        new_string += my_string[i]

    return new_string
