def enter_binary(var_name):
    while True:
        try:
            val = int(input(f"Enter binary for {var_name} (0 or 1): "))
            if val in (0, 1):
                return val
            else:
                print("Musisz wpisać 0 lub 1.")
        except ValueError:
            print("To musi być liczba całkowita (0 lub 1).")

def main():
    x = enter_binary("x")
    y = enter_binary("y")
    z = enter_binary("z")

    print(f"{x} && {y} || {z} | {x and y or z}")
    print(f"{x} && {z} || {y} | {x and z or y}")
    print(f"{y} && {x} || {z} | {y and x or z}")
    print(f"{y} && {z} || {x} | {y and z or x}")
    print(f"{z} && {x} || {y} | {z and x or y}")
    print(f"{z} && {y} || {x} | {z and y or x}")

if __name__ == '__main__':
    main()

