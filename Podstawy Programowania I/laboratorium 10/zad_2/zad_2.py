def factorial(n):
    if n == 0:
        return 1
    else:
        f = n
        while n > 1:
            f *= n - 1
            n -= 1

        return f

def main():
    while True:
        try:
            n = int(input("Enter n: "))
            k = int(input("Enter k: "))

            if not (0 <= k <= n):
                raise ValueError("k should be between 0 and n (inclusive).")
            else:
                break
        except ValueError as err:
            print(err)

    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    print(f"Newton's binomial {n} over {k} is equal to: {numerator / denominator}")

if __name__ == '__main__':
    main()