def readStack(lines: list):
    stack = []
    instructions = []
    stackRead = 0
    for line in lines:
        if line == "":
            stackRead = 1
            continue
        if stackRead == 0:
            stack.append(line)
        else:
            line = line.split(" ")
            instructions.append(line)
    length = len(stack)
    lastLine = stack[length - 1]
    positions = []
    for i in range(len(lastLine)):
        if lastLine[i] == " ":
            continue
        positions.append((int(lastLine[i]), i))

    res = {}
    for i in range(length - 1):
        line = stack[i]
        for pos in positions:
            if pos[1] < len(line) and line[pos[1]] != " ":
                if pos[0] in res:
                    res[pos[0]].append(line[pos[1]])
                else:
                    res[pos[0]] = [line[pos[1]]]
    return res, positions, instructions
