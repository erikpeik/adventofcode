from src.countElfArray import countElfArray

if __name__ == "__main__":
    elfArray = sorted(countElfArray("tests/input.txt"), reverse=True)
    if len(elfArray) >= 3:
        print("The answer is:", elfArray[0] + elfArray[1] + elfArray[2])
    else:
        print("There are not enough elves.")
