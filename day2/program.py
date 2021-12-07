#!/usr/bin/python3

import sys

def part1():
    horizontal = 0
    depth = 0

    for line in sys.stdin.readlines():
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)

        if direction == "forward":
            horizontal += magnitude
        elif direction == "down":
            depth += magnitude
        elif direction == "up":
            depth -= magnitude

    print(horizontal * depth)

def part2():
    horizontal = 0
    depth = 0
    aim = 0

    for line in sys.stdin.readlines():
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)

        if direction == "forward":
            horizontal += magnitude
            depth += aim * magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude

    print(horizontal * depth)


def main():
    part2()
    pass

if __name__ == "__main__":
    main()

