from src.readLines import readLines

if __name__ == "__main__":
    input = readLines("tests/input.txt")
    count = 0
    for first, second in input:
        for i in range(first[1] - first[0] + 1):
            current = first[0] + i
            if current >= second[0] and current <= second[1]:
                count += 1
                break
    print("Result is", count)
