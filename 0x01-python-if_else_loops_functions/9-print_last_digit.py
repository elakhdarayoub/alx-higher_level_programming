#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)[-1]
    print("{:d}".format(int(last)), end='')
    return last
