from src.getLines import getLines

if __name__ == "__main__":
  lines = getLines("tests/input.txt")
  res = 0
  for row in lines:
    row = row.strip()
    if len(row) == 3:
      enemy = ord(row[0]) - 64
      round = ord(row[2]) - 87
      if (enemy < 1 or enemy > 3):
        print("Error: invalid enemy type")
        exit(1)
      if (round == 1):
        res += enemy + 2 if enemy + 2 <= 3 else enemy - 1
      elif (round == 2):
        res += enemy + 3
      elif (round == 3):
        res += (enemy + 1 if enemy < 3 else enemy - 2) + 6
      else:
        print("Error: invalid round type")
        exit(1)
  print ("The answer is:", res)



