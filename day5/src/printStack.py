def printStack(stack: list, positions: list):
    mostBlocks = 0
    for key in stack:
        if len(stack[key]) > mostBlocks:
            mostBlocks = len(stack[key])

    list = []

    for i in range(mostBlocks):
        row = []
        for i in range(len(positions)):
            row.append(" ")
        list.append(row)

    for pos in positions:
        if pos[0] in stack:
            val = stack[pos[0]]
            max = mostBlocks - 1
            for i in range(len(val) - 1, -1, -1):
                list[max][pos[0] - 1] = val[i]
                max -= 1

    for row in list:
        for col in row:
            if col != " ":
                print("[" + str(col) + "] ", end="")
            else:
                print("    ", end="")
        print()
    for pos in positions:
        print(" " + str(pos[0]) + "  ", end="")
    print()
