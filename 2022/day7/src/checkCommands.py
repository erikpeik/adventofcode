def checkCommands(line: str, currentDir: str):
    isLs = 0
    split = line[2:].split(" ")
    if split[0] == "cd":
        if split[1] == "/":
            currentDir = "/"
        elif split[1] == "..":
            if currentDir != "/":
                currentDir = currentDir[0 : currentDir.rfind("/")]
                if currentDir == "":
                    currentDir = "/"
        else:
            currentDir += split[1] if currentDir[-1] == "/" else "/" + split[1]
    elif split[0] == "ls":
        isLs = 1
    return currentDir, isLs
