import sys

if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    lines = fd.readlines()
    fd.close()

    sum = 0
    for row in lines:
        data = row.split(":")
        games = data[1].split(";")
        red = 0
        green = 0
        blue = 0
        for game in games:
            game = game.split(",")
            for val in game:
                values = val.strip().split(" ")
                if values[1] == "blue":
                    if int(values[0]) > blue:
                        blue = int(values[0])
                elif values[1] == "green":
                    if int(values[0]) > green:
                        green = int(values[0])
                elif values[1] == "red":
                    if int(values[0]) > red:
                        red = int(values[0])
        sum += red * green * blue

    print("Result:", sum)
