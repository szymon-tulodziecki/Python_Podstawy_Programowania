def main():
    matrix = [
        [2, 4, 2, 1],
        [4, 2, 1, 3],
        [1, 3, 2, 4],
        [3, 2, 4, 1]
    ]

    arr = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            arr.append(matrix[i][j])

    print(arr)
    sorted_arr = sorted(arr)
    print(sorted_arr)

if __name__ == '__main__':
    main()