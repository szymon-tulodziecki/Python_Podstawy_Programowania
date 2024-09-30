import math
def root(x):
    if x < 0:
        return -math.pow(-x, 1 / 5)
    else:
        return math.pow(x, 1 / 5)

def main():
    x = [-2, -1.5, -1, -0.5, 0, 0.5, 1.5, 2]
    y = []
    for i in range(len(x)):
        y.append(round(root(x[i]), 3))

    print(x)
    print(y)

if __name__ == '__main__':
    main()