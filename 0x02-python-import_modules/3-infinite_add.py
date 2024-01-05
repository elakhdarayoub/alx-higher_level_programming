#!/usr/bin/python3
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    else:
        result = 0
        for i in sys.argv[1:]:
            result += int(i)
        print(result)
