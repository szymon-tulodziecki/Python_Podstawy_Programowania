def wczytajLiczba():
    while True:
        try:
            liczba  = float(input("Podaj liczba typu float: "))
            return liczba
        except ValueError as err:
            print(f"Błąd formatu! {err}")

def main():
    x = wczytajLiczba()
    if (x < 0): print(f"Liczba {x} jest ujemna!")
    elif (x > 0): print(f"Liczba {x} jest nieujemna!")
    else:
        print(f"Liczba {x} jest zerem!")

if __name__ == '__main__':
    main()