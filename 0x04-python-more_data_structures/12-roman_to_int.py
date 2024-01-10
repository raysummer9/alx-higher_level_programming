#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0
    previous_value = 0
    for roman_numeral in reversed(roman_string):
        num = roman_numerals[roman_numeral]
        if num < previous_value:
            result -= num
        else:
            result += num
        previous_value = num

    return result
