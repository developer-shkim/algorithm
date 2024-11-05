import sys

x, y, width, height = map(int, sys.stdin.readline().split())

distances = [x - 0, width - x, y - 0, height - y]
print(min(distances))
