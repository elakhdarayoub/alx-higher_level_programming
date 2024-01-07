#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = []

    if not tuple_a or not tuple_b:
        return None
    # Checking tuple_a
    if len(tuple_a) < 1:
        tuple_a = (0, 0)
    elif len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)

    # Checking tuple_b
    if len(tuple_b) < 1:
        tuple_b = (0, 0)
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)

    for tup in zip(tuple_a, tuple_b):
        result.append(tup[0] + tup[1])
    return tuple(result)

# tuple_a = (1, 89)
# tuple_b = (88, 11)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))
