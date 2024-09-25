import cmath
import numpy as np
import matplotlib.pyplot as plt
def wczytaj_Zmienna(zmienna):
    while True:
        try:
            x_x = int(input(f'Podaj liczba {zmienna}: '))
            return x_x
        except ValueError as err:
            print(err)


def rysuj_wykres(a, b, c, x1, x2):
    # Generujemy wartości x do wykresu
    x = np.linspace(-10, 10, 400)  # 400 punktów między -10 a 10
    y = a * x ** 2 + b * x + c

    # Rysowanie wykresu funkcji kwadratowej
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

    # Oznaczanie miejsc zerowych (rozwiązań równania)
    if x1.imag == 0:  # Tylko jeśli x1 jest rzeczywiste
        plt.scatter([x1.real], [0], color='red', zorder=5)
        plt.text(x1.real, 0, f'x1 = {x1.real:.2f}', fontsize=12, verticalalignment='bottom')
    if x2.imag == 0:  # Tylko jeśli x2 jest rzeczywiste
        plt.scatter([x2.real], [0], color='red', zorder=5)
        plt.text(x2.real, 0, f'x2 = {x2.real:.2f}', fontsize=12, verticalalignment='bottom')

    # Oznaczenie osi i wykresu
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title("Wykres funkcji kwadratowej")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    print("Wczytywanie równania kwadratowego typu: f(x) = ax^2 + bx + c")
    a = wczytaj_Zmienna("a")
    b = wczytaj_Zmienna("b")
    c = wczytaj_Zmienna("c")

    delta = pow(b, 2) - 4 * a * c

    if delta == 0:
        x_0 = (-b) / (2 * a)
        print(f"Podane równaie ma jedno rozwiązanie: x0 = {x_0}")
        rysuj_wykres(a, b, c, x_0, x_0)
    else:
        x_1 = ((-b) - cmath.sqrt(delta)) / (2 * a)
        x_2 = (-b + cmath.sqrt(delta)) / (2 * a)

        print(f"Podane równanie ma 2 rozwiązania x1 = {x_1} oraz x2 = {x_2}")
        rysuj_wykres(a, b, c, x_1, x_2)
if __name__ == '__main__':
    main()