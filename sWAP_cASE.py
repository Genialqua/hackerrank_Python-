def swap_case(s):
    """
    Swap case of characters in the given string.
    >>> swap_case('Hello World!')
    'hELLO wORLD!'
    """
    return ''.join(char.swapcase() for char in s)
