def readLines(fileName: str):
    with open(fileName) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
    return lines
