import sys

n, m = map(int, sys.stdin.readline().split())
result = [0] * n

for i in range(n):
    result[i] = i + 1

for i in range(m):
    bucketOrigin, bucketDestination = map(int, sys.stdin.readline().split())
    result[bucketDestination - 1], result[bucketOrigin - 1] = result[bucketOrigin - 1], result[bucketDestination - 1]

print(*result)
