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

    cards = {}

    for line in lines:
        card = line.strip().split(":")
        id = int(card[0].split(" ")[-1].strip())
        data = card[1].strip().split("|")
        winning = [i.strip() for i in data[0].split(" ") if i]
        our = [i.strip() for i in data[1].split(" ") if i]

        right = []
        for i in our:
            if i in winning:
                right.append(i)
        cards[id] = (len(right), 1)
    for card in cards:
        for i in range(card + 1, card + cards[card][0] + 1):
            if i in cards:
              cards[i] = (cards[i][0], cards[i][1] + cards[card][1])

    res = 0
    for card in cards:
        res += cards[card][1]

    print("Result:", res)






