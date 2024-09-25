def main():
    while True:
        try:
            n = int(input("Enter n: "))
            if n < 0:
                print("n must be positive")
            else:
                break
        except ValueError as err:
            print(err)

    n_n = n

    s = 1
    for i in range(1, n + 1):
        s *= i
        i += 1

    print(s)

    j = 1
    s_s = 1
    while j <= n:
        s_s *= j
        j += 1

    print(s_s)
if __name__ == "__main__":
    main()