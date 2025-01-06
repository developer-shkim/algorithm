import sys
from itertools import combinations


n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))[:n]

# n, m = 10, 500
# numbers = list(map(int, "93 181 245 214 315 36 185 138 216 295".split()))

result = []

for trio in combinations(numbers, 3):
    if sum(trio) <= m:
        result.append(sum(trio))

print(max(result))
