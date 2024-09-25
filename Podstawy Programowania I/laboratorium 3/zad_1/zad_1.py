def wczytajLiczba(v):
    while True:
        try:
            wczytana = float(input(f"{v} ) Podaj liczba: "))
            return wczytana
        except ValueError as err:
            print(err)

def main():
    x = 5
    suma_dodatnich = 0
    suma_ujemnych = 0
    ile_zer = 0

    while x > 0:
        liczba = wczytajLiczba(x)
        if liczba > 0:
            suma_dodatnich += liczba
        elif liczba < 0:
            suma_ujemnych += liczba
        else:
            ile_zer += 1
        x -= 1

    print(f"Suma dodatnich: {suma_dodatnich}")
    print(f"Suma ujemnych: {suma_ujemnych}")
    print(f"Ile zer: {ile_zer}")

if __name__ == '__main__':
    main()
