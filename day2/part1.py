from src.getLines import getLines

def checkRock(enemy):
    if enemy == 1:
        return 3
    elif enemy == 2:
        return 0
    elif enemy == 3:
        return 6
    else:
        print("Error: invalid enemy type")
        exit(1)

def checkPaper(enemy):
  if enemy == 1:
    return 6
  elif enemy == 2:
    return 3
  elif enemy == 3:
    return 0
  else:
    print("Error: invalid enemy type")
    exit(1)

def checkScissors(enemy):
  if enemy == 1:
    return 0
  elif enemy == 2:
    return 6
  elif enemy == 3:
    return 3
  else:
    print("Error: invalid enemy type")
    exit(1)


if __name__ == "__main__":
  lines = getLines("tests/input.txt")

  res = 0
  for row in lines:
    row = row.strip()
    if len(row) == 3:
      enemy = ord(row[0]) - 64
      you = ord(row[2]) - 87
      if (you == 1): # Rock
        res += you + checkRock(enemy)
      elif (you == 2): # Paper
        res += you + checkPaper(enemy)
      elif (you == 3): # Scissors
        res += you + checkScissors(enemy)
      else:
        print("Error: invalid type")
        exit(1)
  print ("The answer is:", res)



