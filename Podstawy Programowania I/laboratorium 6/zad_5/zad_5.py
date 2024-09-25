import random

def main():
    for i in range(1, 6):
        print(f"{random.randrange(100)}")

    print("----------")

    for i in range(1, 10):
        print(f"{random.randint(1, 49)}")

if __name__ == "__main__":
    main()