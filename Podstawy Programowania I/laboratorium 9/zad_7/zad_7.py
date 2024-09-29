import random

def main():
    while True:
        try:
            n_1 = int(input("Enter size of the first array: "))
            n_2 = int(input("Enter size of the second array: "))

            if n_1 <= 0 or n_2 <= 0:
                raise ValueError
            else:
                break
        except ValueError as err:
            print(err)
    arr_1 = [random.randint(1, 51) for _ in range(n_1)]
    arr_2 = [random.randint(1, 51) for _ in range(n_2)]

    arr_1_sorted = sorted(arr_1)
    arr_2_sorted = sorted(arr_2)

    arr_1_2 = arr_1_sorted + arr_2_sorted
    print(arr_1_sorted)
    print(arr_2_sorted)
    print(arr_1_2)
    print(sorted(arr_1_2))

if __name__ == '__main__':
    main()