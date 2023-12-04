def getLines(fileName: str) -> list:
  try:
    fd = open(fileName, "r")
  except Exception as e:
    print("Could not open input file")
    exit(1)
  lines = fd.readlines()
  fd.close()
  return lines
