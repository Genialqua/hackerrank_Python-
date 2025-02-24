def main():
    x = get_int()
    print(f"X is {x}")
def get_int():
    while True:
        try:
            x = int(input("What is x? "))
            break
        except ValueError as e:
            print("Invalid input. Please enter an integer.", e)
    return x
main()  
