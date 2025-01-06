import sys


def minus_one(number):
    return number - 1


n, m = map(int, sys.stdin.readline().split())
boxes = list(range(1, n + 1))

for _ in range(m):
    start, end = map(minus_one, (map(int, sys.stdin.readline().split())))

    while end > start:
        boxes[start], boxes[end] = boxes[end], boxes[start]
        start += 1
        end -= 1

print(*boxes)
