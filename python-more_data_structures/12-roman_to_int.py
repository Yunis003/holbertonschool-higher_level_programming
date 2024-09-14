#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_value = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500
    }

    res = 0
    for val in roman_string:
        if val == None:
            return 0
        else:
            current = roman_value[val]
            res += current
    return res
