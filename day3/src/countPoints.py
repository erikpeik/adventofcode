def countPoints(char: str) -> int:
    char = ord(char)
    if char >=65 and char <= 90:
        char -= 38
    elif char >= 97 and char <= 122:
        char -= 96
    else:
        print("Invalid character")
        exit(1)
    return char
