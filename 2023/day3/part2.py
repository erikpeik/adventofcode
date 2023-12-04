import sys

def _multiply(numbers: list) -> int:
    res = 1
    for num in numbers:
        res *= num
    return res

def _sum(numbers: list) -> int:
    res = 0
    for num in numbers:
        res += num
    return res

def _getTheNumber(line, j):
    num = ""
    while j > 0 and line[j - 1].isnumeric():
        j -= 1
    startj = j
    while j < len(line) and line[j].isnumeric():
        num += line[j]
        j += 1
    return int(num), (startj, j)

def _getNeighbourNumbers(lines: list, i: int, j: int):
    locations = []
    res = []

    if i > 0: # look up
        if lines[i - 1][j].isnumeric() and lines[i - 1][j] != ".":
            num, jlocation = _getTheNumber(lines[i - 1], j)
            if (i - 1, jlocation) not in locations:
                res.append(num)
                locations.append((i - 1, jlocation))
    if j > 0: # look left
        if lines[i][j - 1].isnumeric() and lines[i][j - 1] != ".":
            num, jlocation = _getTheNumber(lines[i], j - 1)
            if (i, jlocation) not in locations:
                res.append(num)
                locations.append((i, jlocation))
    if i < len(lines) - 1: # look down
        if lines[i + 1][j].isnumeric() and lines[i + 1][j] != ".":
            num, jlocation = _getTheNumber(lines[i + 1], j)
            if (i + 1, jlocation) not in locations:
                res.append(num)
                locations.append((i + 1, jlocation))
    if j < len(lines[i]) - 1: # look right
        if lines[i][j + 1].isnumeric() and lines[i][j + 1] != ".":
            num, jlocation = _getTheNumber(lines[i], j + 1)
            if (i, jlocation) not in locations:
                res.append(num)
                locations.append((i, jlocation))
    if i > 0 and j > 0: # look up left
        if lines[i - 1][j - 1].isnumeric() and lines[i - 1][j - 1] != ".":
            num, jlocation = _getTheNumber(lines[i - 1], j - 1)
            if (i - 1, jlocation) not in locations:
                res.append(num)
                locations.append((i - 1, jlocation))
    if i > 0 and j < len(lines[i]) - 1: # look up right
        if lines[i - 1][j + 1].isnumeric() and lines[i - 1][j + 1] != ".":
            num, jlocation = _getTheNumber(lines[i - 1], j + 1)
            if (i - 1, jlocation) not in locations:
                res.append(num)
                locations.append((i - 1, jlocation))
    if i < len(lines) - 1 and j > 0: # look down left
        if lines[i + 1][j - 1].isnumeric() and lines[i + 1][j - 1] != ".":
            num, jlocation = _getTheNumber(lines[i + 1], j - 1)
            if (i + 1, jlocation) not in locations:
                res.append(num)
                locations.append((i + 1, jlocation))
    if i < len(lines) - 1 and j < len(lines[i]) - 1: # look down right
        if lines[i + 1][j + 1].isnumeric() and lines[i + 1][j + 1] != ".":
            num, jlocation = _getTheNumber(lines[i + 1], j + 1)
            if (i + 1, jlocation) not in locations:
                res.append(num)
                locations.append((i + 1, jlocation))

    if len(res) <= 1:
        return 0
    return _multiply(res)


if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    lines = fd.readlines()
    fd.close()

    res = []
    for i in range(0, len(lines)):
        for j in range(0, len(lines[1])):
            if (lines[i][j].isnumeric() == False and lines[i][j] == "*"):
                res.append(_getNeighbourNumbers(lines, i, j))
    print("Result:", _sum(res))
