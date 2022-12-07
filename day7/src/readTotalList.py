from src.readLines import readLines
from src.checkCommands import checkCommands
from src.countValues import countValues


def readTotalList(testFile: str):
    lines = readLines(testFile)
    isLs = 0
    currentDir = ""
    values = {}
    for line in lines:
        if isLs == 1:
            if line[0] == "$":
                currentDir, isLs = checkCommands(line, currentDir)
            else:
                split = line.split(" ")
                if split[0] == "dir":
                    dirInside = (
                        currentDir + split[1]
                        if currentDir[-1] == "/"
                        else currentDir + "/" + split[1]
                    )
                    if currentDir in values:
                        values[currentDir].append(["dir", dirInside])
                    else:
                        values[currentDir] = [["dir", dirInside]]
                else:
                    if currentDir in values:
                        values[currentDir].append([split[1], split[0]])
                    else:
                        values[currentDir] = [[split[1], split[0]]]
        elif line[0] == "$":
            currentDir, isLs = checkCommands(line, currentDir)
    totalList = {}
    for value in values:
        totalList[value] = countValues(values[value], values)
    return totalList
