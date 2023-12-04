from src.readLines import readLines
from src.readStack import readStack
from src.printStack import printStack
from src.moveSupply import moveSupply

if __name__ == "__main__":
    lines = readLines("tests/input.txt")
    stack, positions, instructions = readStack(lines)
    printStack(stack, positions)
    print()
    for instruction in instructions:
        moveSupply(stack, positions, instruction)
        printStack(stack, positions)
        print()
    print("Final message is: ", end="")
    for pos in positions:
        if pos[0] in stack:
            value = stack[pos[0]]
            if len(value) > 0:
                print(value[0], end="")
    print()
