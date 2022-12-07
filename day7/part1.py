from src.readTotalList import readTotalList


if __name__ == "__main__":
    totalList = readTotalList("tests/input.txt")
    lastCount = 0
    print("Total sizes of directories:")
    for value in totalList:
        print(value, totalList[value])
        if totalList[value] <= 100000:
            lastCount += totalList[value]
    print()
    print("Sum of directories with a total size of at most 10000: ", lastCount)
