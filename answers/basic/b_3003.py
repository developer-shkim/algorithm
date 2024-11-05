import sys

chessSets = [1, 1, 2, 2, 2, 8]
inputs = list(map(int, sys.stdin.readline().split()))

for index, value in enumerate(chessSets):
    print(chessSets[index] - inputs[index], end=' ')
