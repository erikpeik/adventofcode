import sys
from helpers.checkIsStringNumber import checkIsStringNumber

if __name__ == "__main__":
  fd = open(sys.argv[1], "r")
  lines = fd.readlines()
  fd.close()

  res = 0
  for row in lines:
    nums = []
    nonnum = ""
    for letter in row.strip():
      if letter.isdigit():
        nums.append(letter)
        nonnum = ""
      else:
        nonnum += letter
        if checkIsStringNumber(nonnum) != None:
          nums.append(checkIsStringNumber(nonnum))
          nonnum = letter
    res += int(str(nums[0]) + str(nums[-1]))
  print("Result:", res)
