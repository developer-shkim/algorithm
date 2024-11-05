import sys

count = int(sys.stdin.readline().strip())

min_x, min_y = map(int, sys.stdin.readline().strip().split())

max_x = min_x
max_y = min_y

for i in range(count-1):
    x, y = map(int, sys.stdin.readline().strip().split())

    if x < min_x:
        min_x = x

    if y < min_y:
        min_y = y

    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y

print((max_x - min_x) * (max_y - min_y))