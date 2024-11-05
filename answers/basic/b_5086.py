import sys

result = []


def check(target, param):
    if param % target == 0:
        return 'factor'
    elif target % param == 0:
        return 'multiple'
    else:
        return 'neither'


while True:
    first, second = map(int, sys.stdin.readline().split())

    if first == 0 and second == 0:
        break

    result.append(check(first, second))

print(*result, sep='\n')
