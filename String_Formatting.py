def print_formatted(number):
    width = len(bin(number)) - 2  # Calculate the width for formatting
    for i in range(1, number + 1):
        print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

print_formatted(17)