#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if not len(sys.argv) == 4:
        for i in sys.argv:
            print(i)
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            result = add(a, b)
            print("{} + {} = {}".format(a, b, result))
        elif sys.argv[2] == '-':
            result = sub(a, b)
            print("{} - {} = {}".format(a, b, result))
        elif sys.argv[2] == '*':
            result = mul(a, b)
            print("{} * {} = {}".format(a, b, result))
        elif sys.argv[2] == '/':
            if not b == 0:
                result = div(a, b)
                print("{} * {} = {}".format(a, b, result))
