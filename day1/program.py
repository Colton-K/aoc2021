#!/usr/bin/python3

def part1():
    numIncreasing = 0
    lines = []

    with open("input.txt", 'r') as fh:
        lines = fh.readlines()

    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            numIncreasing += 1

    print(numIncreasing)

def part2():
    numIncreasing = 0
    lines = []

    with open("input.txt", 'r') as fh:
        lines = fh.readlines()

    for i in range(4, len(lines)):
        curr = sum(map(int, lines[i-4:i-1]))
        next = sum(map(int, lines[i-3:i]))
        print(curr,(lines[i-4:i-1]))
        print(next,(lines[i-3:i]))
        print(curr < next)
        if curr < next:
            numIncreasing += 1

    print(numIncreasing)


def main():
    part2()

if __name__ == "__main__":
    main()

