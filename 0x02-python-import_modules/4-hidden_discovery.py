#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    names = []
    for i in dir(hidden_4):
        if '__' not in i:
            names.append(i)
    names.sort()
    for name in names:
        print(name)
