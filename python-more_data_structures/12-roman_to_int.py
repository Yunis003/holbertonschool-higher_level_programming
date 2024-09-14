#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500
    }
    integer = 0
    prev = 0

    for i in roman_string:
        value = roman_value[i]
        if value == 0:
            return None

        if value > prev:
            integer += value - 2 * prev
        else:
            integer += value
        prev = value
    return integer
