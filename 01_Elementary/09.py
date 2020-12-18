"""
    # All Upper I

    ## Check if a given string has all symbols in upper case.
    ## If the string is empty or doesn't have any letter in it - function should return True.
    
    - Input: A string.

    - Output: a boolean.
"""


def is_all_upper(text: str) -> bool:
    return (lambda text : text.upper() == text)(text)


# These "asserts" are used for self-checking and not for an auto-testing
assert is_all_upper('ALL UPPER') == True
assert is_all_upper('all lower') == False
assert is_all_upper('mixed UPPER and lower') == False
assert is_all_upper('') == True