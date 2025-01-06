import sys


def execution_count2(limit):
    return limit * (limit - 1) * (limit - 2) // 6


def execution_count(limit):
    result = 0

    for i in range(limit, 0, -1):
        result += i * (i + 1) // 2

    return result


num = int(sys.stdin.readline().strip())
print(execution_count(num - 2), 3, sep='\n')
print(execution_count2(num), 3, sep='\n')
