#!/usr/bin/python3
for i in range(1, 100):
    if i >= 10:
        # first, second = tuple(list(str(i)))
        if i % 10 == i // 10 or i > int(str(i)[::-1]):
            continue
    if i != 89:
        print("{:02}, ".format(i), end='')
    else:
        print("{}".format(i))
