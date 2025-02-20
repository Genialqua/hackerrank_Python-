def solve(s):
    # Split input string into separate words
    words = s.split()

    # Capitalize the first letter of each word and join them back together
    s = " ".join(word.capitalize() for word in words)

    # Print the modified string
    print(s)


solve("hello world")