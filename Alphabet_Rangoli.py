def print_rangoli(size):
    # your code goes here
    import string
    
    # Get the lowercase alphabet
    alphabets = string.ascii_lowercase

    # Create a list of the pattern for the given size
    lines = []
    for i in range(size):
        # Select the appropriate slice of alphabets and join with '-'
        s = '-'.join(alphabets[size - 1:i:-1] + alphabets[i:size])
        # Center the pattern with '-'
        lines.append(s.center(4 * size - 3, '-'))

    # Print the rangoli by combining top and bottom parts
    print('\n'.join(lines[::-1] + lines[1:]))