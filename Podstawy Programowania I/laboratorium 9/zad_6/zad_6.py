def main():
    arr = [4, 5, 12, 0, 12, 99, 123, 44, 111, 2, 8, 8]
    arr_sorted = sorted(arr)
    print(arr_sorted)
    if len(arr) % 2 == 1:
        median = arr_sorted[int(len(arr_sorted) / 2)]
        print(median)
    else:
        hlp = int(len(arr_sorted) / 2)
        median = (arr_sorted[hlp] + arr_sorted[hlp - 1]) / 2
        print(median)

if __name__ == '__main__':
    main()