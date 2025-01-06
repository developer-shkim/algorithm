from sys import stdin

n, k = map(int, stdin.readline().split())
scores = sorted(list(map(int, stdin.readline().split())))

print(scores[-k])
