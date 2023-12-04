def moveSupply(stack: dict, positions: list, instruction: list):
    print("Instruction:", instruction)
    for i in range(int(instruction[1])):
        isFrom = int(instruction[3])
        to = int(instruction[5])
        if isFrom in stack:
            if len(stack[isFrom]) > 0:
                if to in stack:
                    stack[to].insert(0, stack[isFrom][0])
                else:
                    stack[to] = [ stack[isFrom][0] ]
                stack[isFrom].pop(0)


