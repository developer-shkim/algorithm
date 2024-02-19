import sys

rows = 9
initValue = -1

maxElement = {'value': initValue, 'row': initValue, 'col': initValue}

for row in range(1, rows+1):
    for col, value in enumerate(map(int, sys.stdin.readline().split()), start=1):
        if maxElement['value'] < value:
            maxElement['value'] = value
            maxElement['row'] = row
            maxElement['col'] = col

print(maxElement['value'])
print(maxElement['row'], maxElement['col'], sep=' ')
