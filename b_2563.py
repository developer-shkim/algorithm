import sys

count = int(sys.stdin.readline().strip())
area = [[False for i in range(100)] for _ in range(100)]

for i in range(count):
    x, y = map(int, sys.stdin.readline().split())

    for j in range(y - 1, y - 1 + 10):
        for k in range(x - 1, x - 1 + 10):
            if area[j][k]:
                pass
            area[j][k] = True

print(sum(area, []).count(True))
