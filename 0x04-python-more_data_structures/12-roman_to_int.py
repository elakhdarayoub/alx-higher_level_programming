#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    romans = {
     "I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000,
     "nan": 0
    }

    integer = 0
    escape = False
    for roman in range(0, len(roman_string)):
        if escape:
            continue
        current = roman_string[roman]
        if roman + 1 < len(roman_string):
            next = roman_string[roman + 1]
        else:
            next = "nan"
        if roman_string[roman] in romans:
            if romans[current] < romans[next]:
                integer += romans[next] - romans[current]
                escape = True
            else:
                integer += romans[current]
                escape = False
    return integer

# roman_number = "X"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "VII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "IX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "LXXXVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))

# roman_number = "DCCVII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
