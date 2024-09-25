def main():
    sumaDodatnich = 0
    sumaUjemnych = 0
    iloscZer = 0

    ile = int(input("Ile liczb chcesz wczytać? \n ->"))
    while ile > 0:
        x = int(input(f"{ile} ) Podaj liczbę: "))
        if x > 0: sumaDodatnich += x
        elif x < 0: sumaUjemnych += x
        else: iloscZer += 1
        ile -= 1

    print(f"Suma dodatnich: {sumaDodatnich}")
    print(f"Suma ujemych: {sumaUjemnych}")
    print(f"Ilość zer: {iloscZer}")

if __name__ == '__main__':
    main()