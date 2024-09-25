from colorama import init, Style, Back, Fore
init()

def main():
    while True:
        try:
            start_temperature = int(input("Enter start temperature: "))
            end_temperature = int(input("Enter end temperature: "))
            if end_temperature < start_temperature:
                print("End temperature must be greater than start temperature")
            else:
                break
        except ValueError:
            print("Invalid input")

    while True:
        try:
            jump = int(input("Enter jump: "))
            if jump < 0:
                print("Jump must be greater than or equal to zero")
            else:
                break
        except ValueError:
            print("Invalid input")

    print(Fore.GREEN + "FAHRENHEIT" + Style.RESET_ALL + Fore.RED + "     CELCIUS" + Style.RESET_ALL)
    while start_temperature < end_temperature:
        print(Fore.GREEN + f"    {start_temperature}" + Style.RESET_ALL + Fore.RED + f"          {round((start_temperature - 32) / 1.8, 2)}" + Style.RESET_ALL)
        start_temperature += jump
if __name__ == "__main__":
    main()