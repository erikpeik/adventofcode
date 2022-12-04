from src.getGroups import getGroups
from src.countPoints import countPoints


def listChars(line: str) -> list:
    chars = []
    for char in line:
        if char not in chars:
            chars.append(char)
    return chars


if __name__ == "__main__":
    groups = getGroups("tests/input.txt")
    res = 0
    for group in groups:
        firstList = listChars(group[0])
        secondList = listChars(group[1])
        thirdList = listChars(group[2])
        for char in firstList:
            if char in secondList and char in thirdList:
                res += countPoints(char)
    print("Result is", res)
