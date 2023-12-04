def checkDuplicates(array: list):
    seen = set()
    for x in array:
        if x in seen:
            return True
        seen.add(x)
    return False


if __name__ == "__main__":
    with open("tests/input.txt") as f:
        data = f.readline().strip()
    print(data)
    res = []
    count = 0
    for char in data:
        count += 1
        if len(res) < 14:
            res.append(char)
        else:
            res.append(char)
            res.pop(0)
        print(res)
        if len(res) == 14 and checkDuplicates(res) == False:
            print(count)
            break
