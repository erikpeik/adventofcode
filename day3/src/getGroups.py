def getGroups(fileName: str) -> list:
    try:
        fd = open(fileName, "r")
    except Exception as e:
        print("Could not open input file")
        exit(1)
    lines = fd.readlines()
    groups = []
    i = 0
    oneGroup = []
    for line in lines:
        line = line.strip()
        oneGroup.append(line)
        i += 1
        if i >= 3:
            i = 0
            groups.append(oneGroup)
            oneGroup = []
    return groups
