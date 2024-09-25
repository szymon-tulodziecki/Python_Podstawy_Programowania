from colorama import init
init()
from colorama import Fore, Back, Style

def main():
    while True:
        try:
            x = int(input("Enter number (0 - 9): "))
            if 0 <= x <= 9:
                if x == 0: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "zero")
                elif x == 1: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "one")
                elif x == 2: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "two")
                elif x == 3: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "three")
                elif x == 4: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "four")
                elif x == 5: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "five")
                elif x == 6: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "six")
                elif x == 7: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "seven")
                elif x == 8: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "eight")
                elif x == 9: print(Fore.GREEN, Back.LIGHTYELLOW_EX + "nine")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED, Back.LIGHTBLUE_EX + f"Enter a number between 0 - 9!")
                print(Style.RESET_ALL)
        except ValueError as err:
            print(err)
if __name__ == "__main__":
    main()