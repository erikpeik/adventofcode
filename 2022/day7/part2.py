from src.readTotalList import readTotalList

if __name__ == "__main__":
    totalList = readTotalList("tests/input.txt")
    totalCount = totalList["/"]
    print("Total size of /: ", totalCount)
    needsToBeFreed = totalCount - 40000000
    print("Needs to be freed:", needsToBeFreed)
    for w in sorted(totalList.items(), key=lambda x: x[1]):
        if w[1] >= needsToBeFreed:
            print("Found it:", w[0], w[1])
            break
