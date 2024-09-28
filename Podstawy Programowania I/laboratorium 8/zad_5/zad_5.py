def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Matrix: ")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print('')
    print('')
    print("Transposition Matrix:")
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            print(f"{matrix[i][j]} ", end = '')
        print('')

if __name__ == '__main__':
    main()