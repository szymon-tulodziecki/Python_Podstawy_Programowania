import random

def main():
    arr = [random.randrange(0, 21) for _ in range(50)]
    print(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)

if __name__ == '__main__':
    main()