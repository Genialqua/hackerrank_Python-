def split_and_join(line):
    line = line.split(" ")
    print(line)

    # Join the words with a hyphen
    hyphenated_line = "-".join(line)
    return (hyphenated_line)


line = input()

print(split_and_join(line))