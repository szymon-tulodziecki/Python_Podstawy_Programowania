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

def main():
    arr = [0] * 6
    enter_data(arr)
    print_data(arr)

if __name__ == '__main__':
    main()