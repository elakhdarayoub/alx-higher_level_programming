#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    result = map(lambda i: i % 2 == 0, my_list)
    return list(result)
