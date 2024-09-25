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
    l_rows = enter_length("rows")
    start = 0
    text = "x"

    while start < l_rows:
        for i in range(0, start):
            print(text, end="")
        print()
        start += 1

if __name__ == "__main__":
    main()