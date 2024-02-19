import sys

n, m = map(int, sys.stdin.readline().split())

results = []

arr = [[input() for j in range(m)] for i in range(n)]

print(*arr)