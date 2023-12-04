def printResult(array: list):
    maxLength = array[0][1] if array[0][1] >= array[1][1] else array[1][1]
    for line in array:
        for i in range(maxLength + 1):
            if i >= line[0] and i <= line[1]:
                print("*", end="")
            else:
                print(".", end="")
        print(" ", line[0], "-", line[1])
    print()
