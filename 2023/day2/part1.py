import sys
from helpers.sum import sum

if __name__ == "__main__":
    fd = open(sys.argv[1], "r")
    lines = fd.readlines()
    fd.close()

    possbileGames = []
    for row in lines:
        data = row.split(":")
        games = data[1].split(";")
        possible = True
        for game in games:
            game = game.split(",")
            for val in game:
                values = val.strip().split(" ")
                if values[1] == "blue":
                    if int(values[0]) > 14:
                        possible = False
                elif values[1] == "green":
                    if int(values[0]) > 13:
                        possible = False
                elif values[1] == "red":
                    if int(values[0]) > 12:
                        possible = False
        if possible:
            possbileGames.append(data[0].strip().split(" ")[-1])

    print("Result:", sum(possbileGames))
