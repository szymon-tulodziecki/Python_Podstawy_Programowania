def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in matrix:
        for column in row:
            print(column, end=' ')
        print("")

if __name__ == '__main__':
    main()