def enter_non_negative_value(number):
    while True:
        try:
            number = int(input(f"Enter {number}: "))
            if number < 0:
                raise ValueError
            else:
                return number
        except ValueError as err:
            print(err)

def main():
    unsigned_a = enter_non_negative_value("a")
    unsigned_b = enter_non_negative_value("b")

    print(f"{unsigned_a} > {unsigned_b}  | {unsigned_a > unsigned_b}")
    print(f"{unsigned_a} >= {unsigned_b} |{unsigned_a >= unsigned_b}")
    print(f"{unsigned_a} < {unsigned_b}  |{unsigned_a < unsigned_b}")
    print(f"{unsigned_a} <= {unsigned_b} |{unsigned_a <= unsigned_b}")
    print(f"{unsigned_a} == {unsigned_b} |{unsigned_a == unsigned_b}")
    print(f"{unsigned_a} != {unsigned_b} |{unsigned_a != unsigned_b}")


if __name__ == "__main__":
    main()

