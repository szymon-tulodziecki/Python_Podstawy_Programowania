from colorama import init, Fore, Style
import random

init()

def main():
    while True:
        try:
            N = int(input("Enter array size N: "))
            if N <= 0:
                print("Array size must be positive")
            else:
                break
        except ValueError as err:
            print(err)

    print("")
    print(Fore.GREEN + f"Randomizing an array of binary numbers..." + Style.RESET_ALL)
    print("")

    a = [0] * N

    for i in range(N):
        a[i] = random.randint(0, 1)

    print("")
    print("The drawn array is:")
    print(a)
    print("")
    string_a = "".join(map(str, a))
    print(f"{string_a}(bin)  = {int(string_a, 2)}(dec)")

    while True:
        try:
            shift = int(input("Enter shift: "))
            if not 0 <= shift <= N:
                print("Shift must be between 0 and N")
            else:
                break
        except ValueError as err:
            print(err)

    print("")

    shift_arr = [0] * shift
    shifted_a = (a + shift_arr)[shift:]

    print("")
    print("The shifted array is:")
    print(shifted_a)
    print("")
    string_shifted_a = "".join(map(str, shifted_a))
    print(f"{string_shifted_a}(bin) = {int(string_shifted_a, 2)}(dec)")

if __name__ == '__main__':
    main()