#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    if n > len(str) - 1 or n < 0:
        return str
    else:
        for i in range(0, len(str)):
            if i == n:
                continue
            else:
                copy += str[i]
    return copy
