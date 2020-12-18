"""
    # Between Markers (simplified)

    ## You are given a string and two markers (the initial one and final).
    ## You have to find a substring enclosed between these two markers.
   
    ## But there are a few important conditions.
    ## -> The initial and final markers are always different.
    ## -> The initial and final markers are always 1 char size.
    ## -> The initial and final markers always exist in a string and go one after another.

    - Input: Three arguments. All of them are strings.
             The second and third arguments are the initial and final markers.

    - Output: A string.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin) + 1:text.find(end)]


# These "asserts" are used for self-checking and not for an auto-testing
assert between_markers('What is >apple<', '>', '<') == "apple"
assert between_markers('What is [apple]', '[', ']') == "apple"
assert between_markers('What is ><', '>', '<') == ""
assert between_markers('>apple<', '>', '<') == "apple"
