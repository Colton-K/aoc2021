#!/usr/bin/python3

import sys

def part1():
    gammaRate = 0
    epsilonRate = 0
    
    binaryInput = sys.stdin.readlines()
    gammabits = []
    for i in range(0, len(binaryInput[0])-1):
        ones = 0
        zeros = 0
        for binary in binaryInput:
            if binary[i] == "1":
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            gammabits.append("1")
        else:
            gammabits.append("0")
    gammaRate = int(''.join(gammabits), 2)
    print(gammabits, gammaRate)
    
    epsilonbits = []
    for bit in gammabits:
        if bit == "1":
            epsilonbits.append("0")
        elif bit == "0":
            epsilonbits.append("1")
    epsilonRate = int(''.join(epsilonbits), 2)
    print(epsilonbits, epsilonRate)

    powerConsumption = epsilonRate * gammaRate
    print(powerConsumption)

def part2():
    binaryInput = [line.rstrip() for line in sys.stdin.readlines()]
    binaryInput2 = binaryInput.copy()
    #  binaryInput = sys.stdin.readlines()
    currBit = 0
    while len(binaryInput) > 1:
        # find right things 
        counts = [0 for _ in range(0, len(binaryInput[0]))]
        for line in binaryInput:
            for i, binary in enumerate(line):
                counts[i] += int(binary)
        selected = ["1" if count >= len(binaryInput)/2 else "0" for count in counts]
        #  for i in range(0,len(ones)):
        #      if ones[i] >= zeros[i]:
        #          selected.append("1")
        #      else:
        #          selected.append("0")

        # cut things
        binaryInput = [i for i in binaryInput if i[currBit] == selected[currBit]]
        #  newInput = []
        #  for number in binaryInput:
        #      print(number, currBit, selected)
        #      if number[currBit] == selected[currBit]:
        #          newInput.append(''.join(number))
        #  binaryInput = newInput
        # -------------

        #  print(binaryInput)
        currBit += 1

    oxygenGenRating = (int(binaryInput[0], 2))


    currBit = 0
    while len(binaryInput2) > 1:
        # find right things 
        counts = [0 for _ in range(0, len(binaryInput2[0]))]
        for line in binaryInput2:
            for i, binary in enumerate(line):
                counts[i] += int(binary)
        selected = ["1" if count < len(binaryInput2)/2 else "0" for count in counts]
        #  for i in range(0,len(ones)):
        #      if ones[i] >= zeros[i]:
        #          selected.append("1")
        #      else:
        #          selected.append("0")

        # cut things
        binaryInput2 = [i for i in binaryInput2 if i[currBit] == selected[currBit]]
        #  newInput = []
        #  for number in binaryInput2:
        #      print(number, currBit, selected)
        #      if number[currBit] == selected[currBit]:
        #          newInput.append(''.join(number))
        #  binaryInput2 = newInput
        # -------------

        #  print(binaryInput2)
        currBit += 1
    
    co2scrubberRating = (int(binaryInput2[0], 2))
    

    lifeSupportRating = oxygenGenRating * co2scrubberRating
    print(lifeSupportRating)

def main():
    part2()
    pass

if __name__ == "__main__":
    main()

