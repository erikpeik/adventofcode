import sys

def _checkNeighbours(lines: list, i: int, j: int, val: str) -> bool:
    anySymbol = False
    length = len(val)

    lines = [line.strip() for line in lines]

    while length > 0:
        if i > 0: # look up
            if lines[i - 1][j].isnumeric() == False and lines[i - 1][j] != ".":
                anySymbol = True
        if j > 0: # look left
            if lines[i][j - 1].isnumeric() == False and lines[i][j - 1] != ".":
                anySymbol = True
        if i < len(lines) - 1: # look down
            if lines[i + 1][j].isnumeric() == False and lines[i + 1][j] != ".":
                anySymbol = True
        if j < len(lines[i]) - 1: # look right
            if lines[i][j + 1].isnumeric() == False and lines[i][j + 1] != ".":
                anySymbol = True
        if i > 0 and j > 0: # look up left
            if lines[i - 1][j - 1].isnumeric() == False and lines[i - 1][j - 1] != ".":
                anySymbol = True
        if i > 0 and j < len(lines[i]) - 1: # look up right
            if lines[i - 1][j + 1].isnumeric() == False and lines[i - 1][j + 1] != ".":
                anySymbol = True
        if i < len(lines) - 1 and j > 0: # look down left
            if lines[i + 1][j - 1].isnumeric() == False and lines[i + 1][j - 1] != ".":
                anySymbol = True
        if i < len(lines) - 1 and j < len(lines[i]) - 1: # look down right
            if lines[i + 1][j + 1].isnumeric() == False and lines[i + 1][j + 1] != ".":
                anySymbol = True
        j -= 1
        length -= 1
    return anySymbol


if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    lines = fd.readlines()
    fd.close()

    res = []
    for i in range(0, len(lines)):
        num = ""
        for j in range(0, len(lines[1])):
            if (lines[i][j].isnumeric()):
                num += lines[i][j]
            else:
                if num != "":
                    if _checkNeighbours(lines, i, j - 1, num):
                        res.append(int(num))
                    num = ""
    print("Result:", sum(res))
