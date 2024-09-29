def main():
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    arr.sort()

    unique_values = []
    counts = []

    current_value = None
    count = []

    for value in arr:
        if value == current_value:
            count += 1
        else:
            if current_value is not None:
                unique_values.append(current_value)
                counts.append(count)
            current_value = value
            count = 1

    if current_value is not None:
        unique_values.append(current_value)
        counts.append(count)

    print("Unique values: ", unique_values)
    print("Counts :", counts)

if __name__ == '__main__':
    main()