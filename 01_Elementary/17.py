"""
    # Is Even

    ## Check if the given number is even or not.
    ## Your function should return True if the number is even, and False if the number is odd. 
   
    - Input: An int.
    - Output: A bool.

    >> EXAMPLE:
       
        is_even(2) == True
        is_even(5) == False
        is_even(0) == True
    
    <<
"""


def is_even(num: int) -> bool:
    return bool(num % 2 == 0)


# These "asserts" are used for self-checking and not for an auto-testing
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True
