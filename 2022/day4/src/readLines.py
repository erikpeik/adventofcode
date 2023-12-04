def readLines(fileName: str):
    with open(fileName) as f:
        lines = f.readlines()
        res = []
        for line in lines:
            line = line.strip()
            line = line.split(",")
            newline = []
            for item in line:
                item = item.split("-")
                item = [int(item[0]), int(item[1])]
                newline.append(item)
            res.append(newline)
    return res
