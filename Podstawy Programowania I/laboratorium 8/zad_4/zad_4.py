def main():
    while True:
        try:
            m = int(input('Enter m: '))

            if 0 >= m:
                print('Enter positive integer')
            else:
                break
        except ValueError as err:
            print(err)

    matrix = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

    print(f"Unit matrix {m} x {m}: ")

    for i in range(m):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print('')

if __name__ == "__main__":
    main()