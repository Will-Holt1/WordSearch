import random as rand
from array import *

BOLD = '\033[1m'
END = '\033[0m'
lETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"


def main():
    dict = open("Dictionary.txt", "r")
    words = dict.readlines()
    length = 10
    width = 30
    height = 15
    wordBank = []
    grid = [['A'] * height for i in range(width)]



    for n in range(length):
        wordBank.append(words[rand.randint(0, len(words))][:-1])

    for y in range(height):
        for x in range(width):
            grid[x][y] = lETTERS[rand.randint(0, 25)]

    for y in range(height):
        print("\n")
        for x in range(width):
            print(grid[x][y], end="\t")

    result = ''
    for c in "text":
        result = result + c + '\u0336'

    print(result)






main()
