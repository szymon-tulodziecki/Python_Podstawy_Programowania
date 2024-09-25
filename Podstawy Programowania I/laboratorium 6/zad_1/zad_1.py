def main():
    while True:
        try:
            n = int(input("Enter n: "))
            if n < 1:
                raise ValueError
                print("Enter a positive integer")
            else:
                break
        except:
            print("Enter a positive integer")


    i = 1
    sum_of_elements = 0

    while i <= n:
        while True:
            try:
                element = int(input(f"{i}) Enter element: "))
                sum_of_elements += element
                break
            except ValueError:
                print("Enter a positive integer")
        i += 1

    print(f"Sum of given elements: {sum_of_elements}")


if __name__ == "__main__":
    main()