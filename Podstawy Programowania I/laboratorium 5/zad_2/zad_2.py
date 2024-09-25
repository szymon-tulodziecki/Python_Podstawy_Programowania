def enter_non_negative_value(var_name):
    while True:
        try:
            number = int(input(f"Enter {var_name}: "))
            if number < 0:
                raise ValueError("Value must be positive!")
            return number
        except ValueError as err:
            print(err)

def main():
    a = enter_non_negative_value("a")
    b = enter_non_negative_value("b")

    print(f"{a} && {b}                 | {a and b}")
    print(f"{a} || {b}                 | {a or b}")
    print(f"!{a}                       | {not a} ")
    print(f"!{b}                       | {not b}")
    print(f"!{a} && {b}                | {not a and b}")
    print(f"!{a} && {b} || {a} && !{b} | {not a and b or a and not b}")

if __name__ == '__main__':
    main()
