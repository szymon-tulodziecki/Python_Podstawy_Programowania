def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    while True:
        try:
            row_a = int(input('Row a: '))
            row_b = int(input('Row b: '))

            if not 0 <= row_a < len(matrix[0]) or not 0 <= row_b < len(matrix):
                raise ValueError
            else:
                break
        except ValueError:
            print('There are not that rows!')


    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end=' ')
        print('')

    print('')

    for i in range(0, len(matrix)):
        matrix[row_a][i], matrix[row_b][i] = matrix[row_b][i], matrix[row_a][i]


    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end=' ')
        print('')

    print('')

if __name__ == '__main__':
    main()