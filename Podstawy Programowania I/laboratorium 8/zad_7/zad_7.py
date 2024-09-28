def main():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}  ", end=" ")
        print("")

    print("")

    while True:
        try:
            col_a = int(input("Enter column a: "))
            col_b = int(input("Enter column b: "))

            if not (0 <= col_a < len(matrix[0]) and 0 <= col_b < len(matrix)):
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid input")

    print("")

    for i in range(len(matrix)):
        matrix[i][col_a], matrix[i][col_b] = matrix[i][col_b], matrix[i][col_a]
    print("")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}  ", end=" ")
        print("")

if __name__ == "__main__":
    main()
