def countValues(values: list, totalList: dict):
    sum = 0
    for value in values:
        if value[0] == "dir":
            sum += countValues(totalList[value[1]], totalList)
        else:
            sum += int(value[1])
    return sum
