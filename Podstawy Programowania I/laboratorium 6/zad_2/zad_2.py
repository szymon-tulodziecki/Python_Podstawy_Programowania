from colorama import init
init()
from colorama import Fore, Back, Style

def main():
    start = 20
    stop = 300

    print(Fore.RED + "CELCIUS" + Style.RESET_ALL + Fore.GREEN + " FAHRENHEIT" + Style.RESET_ALL)
    while start < stop:
        print(Fore.RED + f"  {start}" + Style.RESET_ALL, Fore.GREEN + f"     {round(start * 1.8 + 32, 2)}" + Style.RESET_ALL)
        print()
        start += 1

if __name__ == '__main__':
    main()