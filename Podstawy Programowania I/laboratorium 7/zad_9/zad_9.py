arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("------")
print(arr_1, "\n" + str(arr_2))

for i in range(len(arr_1)):
    hlp = arr_1[i]
    arr_1[i] = arr_2[i]
    arr_2[i] = hlp
print("------")
print(arr_1, "\n" + str(arr_2))
