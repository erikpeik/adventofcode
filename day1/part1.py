from src.countElfArray import countElfArray

if __name__ == "__main__":
    elfArray = countElfArray("tests/input.txt")
    print("The answer is:", max(elfArray))
