def main():
    while True:
        try:
            N = int(input("Enter array size: "))

            if N <= 0:
                print("Array size must be greater than zero.")
            else:
                break
        except ValueError as err:
            print(err)

    arr = [0] * N

    for i in range(N):
        while True:
            try:
                arr[i] = float(input(f"Enter arr[{i}]: "))
                break
            except ValueError as err:
                print(err)


    print(f"Array is {arr}")
    print("")

    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)

if __name__ == "__main__":
    main()


