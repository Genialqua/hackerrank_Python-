def mutate_string(string, position, character):
    # Convert the string to a list
    string_list = list(string)

    # Replace the character at the specified position
    string_list[position] = character

    # Convert the list back to a string
    mutated_string = "".join(string_list)

    return mutated_string
