#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    quotion = 0
    for i in range(0, list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            quotion = a / b
        except ZeroDivisionError:
            print("division by 0")
            quotion = 0
        except IndexError:
            print("out of range")
            quotion = 0
        except TypeError:
            print("wrong type")
            quotion = 0
        finally:
            new_list.append(quotion)
    return new_list
