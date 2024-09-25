def main():
    arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr_2 = []

    for i in range (len(arr_1)):
        if i % 2 == 0:
            arr_2.append(arr_1[i])

    print(arr_1)
    print("-------")
    print(arr_2)

if __name__ == '__main__':
    main()
