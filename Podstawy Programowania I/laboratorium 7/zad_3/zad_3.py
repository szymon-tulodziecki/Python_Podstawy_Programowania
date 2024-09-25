def enter_data(arr_x):
    for i in range(len(arr_x)):
        while True:
            try:
                arr_x[i] = int(input(f"Enter array[{i}]: "))
                break
            except ValueError as err:
                print(err)

def print_data(arr_x):
    for i in range(len(arr_x)):
        print(f"array[{i}]: {arr_x[i]}")

def sum_array(arr_x):
    sum_a, sum_e, sum_o = 0, 0, 0

    for i in range(len(arr_x)):
        sum_a += arr_x[i]
        if arr_x[i] % 2 == 0: sum_e += arr_x[i]
        else: sum_o += arr_x[i]

    return sum_a, sum_e, sum_o

def main():
    arr = [0] * 6
    enter_data(arr)
    print_data(arr)
    sum_all, sum_even, sum_odd = sum_array(arr)

    print(f"Sum of array: {sum_all} \n Sum of even in array: {sum_even} \n Sum of odd in array: {sum_odd}")
if __name__ == '__main__':
    main()