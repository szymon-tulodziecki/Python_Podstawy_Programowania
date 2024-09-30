def dMultiply(a, b):
    return a * b

def dDivide(a, b):
    z = float(a / b)
    return z
def dAdd(a, b):
    return a + b

def dSubtract(a, b):
    return a - b

def main():
    x, y = 123, 23

    sum = dAdd(x, y)
    print(f"Sum of {x} and {y} is {sum}")

    subtract = dSubtract(x, y)
    print(f"Difference of {x} and {y} is {subtract}")

    multiply = dMultiply(x, y)
    print(f"Difference of {x} and {y} is {multiply}")

    divide = dDivide(x, y)
    print(f"Divided {x} and {y} is {round(divide, 2)}")

if __name__ == '__main__':
    main()