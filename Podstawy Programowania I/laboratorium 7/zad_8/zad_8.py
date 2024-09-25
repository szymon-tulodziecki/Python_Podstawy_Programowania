arr = [0] * 10

for i in range(10):
    while True:
        try:
            arr[i] = int(input(f"arr[{i}] = "))
            break
        except ValueError as err:
            print(err)

print(f"Minimum: {min(arr)}")
print(f"Maximum: {max(arr)}")