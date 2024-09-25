def ile_osob(nr_sali):
    while True:
        try:
            x = int(input(f"Wprowadź ilość osób w sali nr. {nr_sali} \n-> "))
            if x < 0:
                print("Ilość osób w sali nie może być ujemna!")
            else:
                return x
                break
        except ValueError as err:
            print(err)

def sprawdz_ilosc(ilosc, nr):
    if nr == "1":
        if ilosc >= 1 and ilosc <= 100:
            print(f"W sali nr. {nr} jest prawidłowa ilość osób!")
        elif ilosc >= 100:
            print(f"W sali nr. {nr} jest o {abs(ilosc - 100)} osób za dużo!")
    elif nr == "2":
        if ilosc >= 2 and ilosc <= 60:
            print(f"W sali nr. {nr} jest prawidłowa ilość osób!")
        elif ilosc < 2:
            print(f"W sali nr. {nr} jest o {abs(ilosc - 2)} osób za mało!")
        elif ilosc > 60:
            print(f"W sali nr. {nr} jest o {abs(ilosc - 60)} osób za duzó!")
    elif nr == "3":
        if ilosc >= 3 and ilosc <= 50:
            print(f"W sali nr. {nr} jest prawidłowa ilość osób!")
        elif ilosc < 3:
            print(f"W sali nr. {nr} jest o {abs(ilosc - 3)} osób za mało!")
        elif ilosc > 50:
            print(f"W sali nr. {nr} jest o {abs(ilosc - 50)} osób za dużo!")

def main():
    print("SALA nr.1 ")
    ilosc_osob_sala1  = ile_osob("1")
    sprawdz_ilosc(ilosc_osob_sala1, "1")

    print("SALA nr.2 ")
    ilosc_osob_sala2  = ile_osob("2")
    sprawdz_ilosc(ilosc_osob_sala2, "2")

    print("SALA nr.3 ")
    ilosc_osob_sala3  = ile_osob("3")
    sprawdz_ilosc(ilosc_osob_sala3, "3")

if __name__ == "__main__":
    main()