def moveSupply(stack: dict, positions: list, instruction: list):
    print("Instruction:", instruction)

    isFrom = int(instruction[3])
    to = int(instruction[5])
    movingSupply = []
    for i in range(int(instruction[1])):
        if isFrom in stack:
            if len(stack[isFrom]) > 0:
                movingSupply.append(stack[isFrom][0])
                stack[isFrom].pop(0)
    print("Moving supply:", movingSupply)
    for i in range(len(movingSupply) - 1, -1, -1):
        if to in stack:
            stack[to].insert(0, movingSupply[i])
        else:
            stack[to] = [ movingSupply[i] ]
