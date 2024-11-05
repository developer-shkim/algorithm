import itertools
import sys

rows = 5
result = []

for _ in range(rows):
    for col, value in enumerate(list(sys.stdin.readline().strip())):
        if len(result) > col:
            result[col].append(value)
        else:
            result.append([value])

print(*list(itertools.chain(*result)), sep='')
