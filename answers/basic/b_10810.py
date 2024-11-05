import sys

n, m = map(int, sys.stdin.readline().split())
result = [0] * n

for i in range(m):
    start, end, ballNumber = map(int, sys.stdin.readline().split())
    for j in range(start - 1, end):
        result[j] = ballNumber

print(*result)
