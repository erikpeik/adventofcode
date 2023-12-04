def checkIsStringNumber(value: str = None) -> int | None:
  if "one" in value:
    return 1
  elif "two" in value:
    return 2
  elif "three" in value:
    return 3
  elif "four" in value:
    return 4
  elif "five" in value:
    return 5
  elif "six" in value:
    return 6
  elif "seven" in value:
    return 7
  elif "eight" in value:
    return 8
  elif "nine" in value:
    return 9
  elif "zero" in value:
    return 0
  else:
    return None

