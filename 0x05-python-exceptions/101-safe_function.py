#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(args[0], args[1])
        return result
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
