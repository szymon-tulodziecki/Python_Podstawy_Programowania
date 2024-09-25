import re

def is_octal(f_octal):
    return bool(re.match(r'^[0-7]+$', f_octal))

def is_hexadecimal(f_hexadecimal):
    return bool(re.match(r'^[0-9A-Fa-f]+$', f_hexadecimal))

def enter_decimal():
    while True:
        try:
            x = int(input("-> "))
            return x
        except ValueError:
            print("Given input is not a valid decimal number!")

def enter_octal():
    while True:
        x = input("-> ")
        if is_octal(x):
            return x
        else:
            print("Given input is not octal!")

def enter_hexadecimal():
    while True:
        x = input("-> ")
        if is_hexadecimal(x):
            return x
        else:
            print("Given input is not hexadecimal!")

def main():
    list_1 = [0] * 5
    list_2 = [0] * 5
    list_3 = [0] * 5

    print("Enter Decimal Numbers!")
    for i in range(len(list_1)):
        list_1[i] = enter_decimal()

    print("Enter Octal Numbers!")
    for j in range(len(list_2)):
        list_2[j] = enter_octal()

    print("Enter Hexadecimal Numbers!")
    for k in range(len(list_3)):
        list_3[k] = enter_hexadecimal()

    print("Decimal Numbers:", list_1)
    print("Octal Numbers:", list_2)
    print("Hexadecimal Numbers:", list_3)

if __name__ == "__main__":
    main()
