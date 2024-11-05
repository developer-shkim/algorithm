import sys

divisor = 42
countOfNumber = 10
inputtedNumbers = []

for i in range(countOfNumber):
    inputtedNumber = int(sys.stdin.readline())
    if inputtedNumber % divisor not in inputtedNumbers:
        inputtedNumbers.append(inputtedNumber % divisor)

print(len(inputtedNumbers))