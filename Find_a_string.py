def count_substring(string, sub_string):
    # Initialize a counter to keep track of the number of occurrences
    count = 0

    # Find all occurrences of the sub_string in the string
    start = string.find(sub_string)
    while start != -1:
        count += 1
        start = string.find(sub_string, start + 1)  # Move one step forward

    return count
