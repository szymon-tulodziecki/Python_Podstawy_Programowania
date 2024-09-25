def wczytaj_liczba(wartosc):
    while True:
        try:
            x = int(input(f"Podaj wartość: {wartosc}: "))
            return x
        except ValueError as err:
            print(f"Błąd: {err}. Wprowadź poprawną wartość!")


def main():
    x = wczytaj_liczba("x")
    y = wczytaj_liczba("y")

    print(f"x^2 = {pow(x, 2)} ")
    print(f"x / y = {x / y}")
    print(f"abs(x) = {abs(x)}")
    print(f"x^3 = {pow(x, 3)}")
    
if __name__ == '__main__':
    main()