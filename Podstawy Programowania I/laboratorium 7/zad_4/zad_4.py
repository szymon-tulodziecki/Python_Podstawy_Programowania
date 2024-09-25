from colorama import init, Fore, Style
init()

def enter_array(arr_x):
    for i in range(len(arr_x)):
        while True:
            try:
                arr_x[i] = float(input(f"Enter array[{i}]: "))
                break
            except ValueError as err:
                print(Fore.RED + f"{err}" + Style.RESET_ALL)

def sum_array(array_x, min_v, max_v, min_ind, max_ind):
    sum_p, sum_n, sum_r, sum_ri = 0, 0, 0, 0

    for i in range(len(array_x)):
        if array_x[i] > 0:
            sum_p += array_x[i]
        elif array_x[i] < 0:
            sum_n += array_x[i]

        if min_v <= array_x[i] <= max_v:
            sum_r += array_x[i]

        if min_ind <= i <= max_ind:
            sum_ri += array_x[i]

    return sum_p, sum_n, sum_r, sum_ri

def main():
    arr = [0] * 8
    enter_array(arr)

    while True:
        try:
            min_value = float(input("Enter min value: "))
            max_value = float(input("Enter max value: "))

            if min_value >= max_value:
                print(Fore.RED + f"Min value {min_value} must be less than max value {max_value}" + Style.RESET_ALL)
                continue
            else:
                break
        except ValueError as err:
            print(Fore.RED + f"Invalid input. Please enter a valid number." + Style.RESET_ALL)

    while True:
        try:
            min_index = int(input("Enter min index (0-7): "))
            max_index = int(input("Enter max index (0-7): "))

            if min_index >= max_index:
                print(Fore.RED + f"Min index {min_index} must be less than max index {max_index}" + Style.RESET_ALL)
            elif not (0 <= min_index <= 7) or not (0 <= max_index <= 7):
                print(Fore.RED + f"Indexes must be between 0 and 7." + Style.RESET_ALL)
            else:
                break
        except ValueError as err:
            print(Fore.RED + f"Invalid input. Please enter a valid integer." + Style.RESET_ALL)

    sum_positive, sum_negative, sum_range, sum_range_index = sum_array(arr, min_value, max_value, min_index, max_index)

    print(f"Sum of:")
    print(f"- positive elements: {sum_positive}")
    print(f"- negative elements: {sum_negative}")
    print(f"- elements with value in range ({min_value} - {max_value}): {sum_range}")
    print(f"- elements with index in range ({min_index} - {max_index}): {sum_range_index}")

if __name__ == '__main__':
    main()
