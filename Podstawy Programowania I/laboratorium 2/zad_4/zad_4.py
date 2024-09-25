def wczytaj_liczba(liczba):
    while True:
        try:
            z = float(input(f"Podaj liczba {liczba}: "))
            return z
        except ValueError as err:
            print(err)

def main():
    x = wczytaj_liczba("x")
    y = wczytaj_liczba("y")

    print(f"Suma {x} i {y} jest równa: {x + y}")
if __name__ == '__main__':
    main()