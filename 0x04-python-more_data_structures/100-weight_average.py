#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    divisor = 0

    for item in list(map(lambda tup: tup[0] * tup[1], my_list)):
        total += item
    for element in list(map(lambda y: y[1], my_list)):
        divisor += element
    return total / divisor
