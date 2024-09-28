def main():
    m, n = 2, 4
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            while True:
                try:
                    matrix[i][j] = int(input(f"matrix[{i},{j}]: "))
                    break
                except ValueError as err:
                    print(err)

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print("")

if __name__ == '__main__':
    main()