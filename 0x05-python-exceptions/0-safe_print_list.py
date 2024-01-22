#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for ele in range(0, x):
            print("{}".format(my_list[ele]), sep='', end='')
            counter += 1
    except IndexError:
        pass
    print()
    return counter
