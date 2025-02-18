def floor_mat(floor_width, height=None):
    # Ensure floor_width is an odd number
    if floor_width % 2 == 0:
        print("Width must be an odd number.")
        return

    # Set height if not provided
    if height is None:
        height = floor_width * 3  # Standard formula for height

    # Create the pattern
    for i in range(1, floor_width, 2):
        print((".|." * i).center(height, "-"))

    # Print "WELCOME" in the center
    print("WELCOME".center(height, "-"))

    # Reverse the top pattern to form the bottom half
    for i in range(floor_width - 2, 0, -2):
        print((".|." * i).center(height, "-"))


floor_mat(7, 21)