#!/usr/bin/python3
def uppercase(str):
    copy = ''
    for c in str:
        if ord(c) in range(97, 123):
            copy += chr(ord(c) - 32)
        else:
            copy += c
    print("{}".format(copy))
uppercase("Hello world!")
