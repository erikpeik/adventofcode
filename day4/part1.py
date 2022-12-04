from src.readLines import readLines
from src.printResult import printResult

if __name__ == "__main__":
    input = readLines("tests/input.txt")
    count = 0
    for line in input:
        first = line[0]
        second = line[1]
        if (first[0] >= second[0] and first[1] <= second[1]) or (
            second[0] >= first[0] and second[1] <= first[1]
        ):
            printResult(line)
            count += 1
    print("Result is", count)
