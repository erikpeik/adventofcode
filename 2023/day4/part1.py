import sys

def _getResult(num: int) -> int:
    if num == 0:
        return 0
    res = 1
    for i in range(1, num):
        res += res
    return res


def _sum(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total

if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    lines = fd.readlines()
    fd.close()

    res = []
    for line in lines:
        card = line.strip().split(":")
        data = card[1].strip().split("|")
        winning = [i.strip() for i in data[0].split(" ") if i]
        our = [i.strip() for i in data[1].split(" ") if i]
        right = []

        for i in our:
            if i in winning:
                right.append(i)
        res.append(_getResult(len(right)))

    print("Result:", _sum(res))






