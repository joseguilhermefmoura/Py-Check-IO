"""
    # Replace First

    ## In a given list the first element should become the last one.
    ## An empty list or list with only one element should stay the same.
    
    - Input: List.

    - Output: Iterable.
"""


def replace_first(items: list) -> list:
    if not items:
        return []
    else:
        items.append(items[0])
        return items[1:]

# These "asserts" are used for self-checking and not for an auto-testing
assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
assert list(replace_first([1])) == [1]
assert list(replace_first([])) == []