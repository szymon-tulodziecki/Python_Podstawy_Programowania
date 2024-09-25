def enter_length(l_name):
    while True:
        try:
            l_value = int(input(f"Enter number of {l_name}: "))
            if l_value <= 0:
                raise ValueError
            else:
                return l_value
        except ValueError as err:
            print(err)
            print("Enter number value!")

def main():
    l_cols = enter_length("cols")
    l_rows = enter_length("rows")

    for i in range(0, l_cols):
        for j in range(0, l_rows):
            print("x", end = " ")
        print()
if __name__ == "__main__":
    main()