import sys

count = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

maxScore = max(scores)
total = 0

for i in range(count):
    total += scores[i] / maxScore * 100

print(total / len(scores))