from src.getLines import getLines
from src.countPoints import countPoints

if __name__ == "__main__":
    lines = getLines("tests/input.txt")
    res = 0
    for line in lines:
        line = line.strip()
        firstPart, secondPart = line[: len(line) // 2], line[len(line) // 2 :]
        newList = []
        for char in firstPart:
            if char in secondPart and char not in newList:
                newList.append(char)
        for char in newList:
            res += countPoints(char)
    print("Result is", res)
