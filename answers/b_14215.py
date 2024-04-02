import sys

sides = list(map(int, sys.stdin.readline().strip().split()))

maxOfSide = max(sides)
sumOfSides = sum(sides)

if maxOfSide >= sumOfSides - maxOfSide:
    print((sumOfSides - maxOfSide) * 2 - 1)
else:
    print(sumOfSides)
