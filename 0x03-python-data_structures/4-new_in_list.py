#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None
    copy_list = [e for e in my_list]
    if not idx < 0 and not idx >= len(my_list):
        copy_list[idx] = element
    return copy_list
