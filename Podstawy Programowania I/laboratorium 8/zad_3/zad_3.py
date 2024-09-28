from colorama import init, Fore, Back, Style

init()

def main():
    m, n = 3, 3

    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            while True:
                try:
                    matrix[i][j] = int(input(f"matrix[{i},{j}]: "))
                    break
                except ValueError as err:
                    print(Fore.RED + f"{err}" + Style.RESET_ALL)
    print("")
    while True:
        try:
            selected_row = int(input(f"Enter number of row to sum: "))
            selected_col = int(input(f"Enter number of column to sum: "))

            if 0 <= selected_row < m and 0 <= selected_col < n:
                break
            else:
                print(Fore.RED + f"Invalid input!" + Style.RESET_ALL)
        except ValueError as err:
            print(Fore.RED + f"{err}" + Style.RESET_ALL)

    sum_of_row = sum(matrix[selected_row])
    sum_of_col = sum(matrix[i][selected_col] for i in range(m))

    print("")

    for i in range(m):
        for j in range(n):
            print(f"{matrix[i][j]} ", end = "")
        print("")

    print("")

    print(f"Sum of rows: {sum_of_row}")
    print(f"Sum of columns: {sum_of_col}")

if __name__ == '__main__':
    main()