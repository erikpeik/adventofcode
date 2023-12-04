import sys

if __name__ == "__main__":
  fd = open(sys.argv[1], "r")
  lines = fd.readlines()
  fd.close()

  res = 0
  for row in lines:
    nums = []
    for letter in row.strip():
      if letter.isdigit():
        nums.append(letter)
    res += int(nums[0] + nums[-1])
  print("Result:", res)
