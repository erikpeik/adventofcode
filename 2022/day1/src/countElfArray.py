def countElfArray(testFile: str = None) -> list:
    fd = open(testFile, "r")
    lines = fd.readlines()
    fd.close()

    elfArray = []
    result = 0
    for row in lines:
        if row.strip() == "":
            elfArray.append(result)
            result = 0
        else:
            result += int(row.strip())
    return elfArray
