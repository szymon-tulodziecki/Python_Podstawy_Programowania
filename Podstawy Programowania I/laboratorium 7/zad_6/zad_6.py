from colorama import init, Fore, Style
init()
def red_on():
    print(Fore.RED)

def color_off():
    print(Style.RESET_ALL)

def main():
    arr = [0] * 5

    for i in range(5):
        while True:
            try:
                arr[i] = float(input(f"arr[{i}] = "))
                break
            except ValueError as err:
                red_on()
                print(err)
                color_off()


    while True:
        try:
            index_1 = int(input(f"Enter first index (0 - 5): "))
            index_2 = int(input(f"Enter second index (0 - 5): "))

            if index_1 == index_2:
                print(f"We can't switch same index!")
                raise ValueError
            elif not 0 <= index_1 < 5 or not 0 <= index_2 < 5:
                print(f"We can't switch not existing indexes!")
                raise ValueError
            else:
                break
        except ValueError as err:
            red_on()
            print(err)
            color_off()

    print(arr)

    hlp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = hlp

    print(arr)

    print(f"{max(arr)}")
    print(f"{min(arr)}")
if __name__ == "__main__":
    main()