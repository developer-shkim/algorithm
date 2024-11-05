import sys


def reverse_func(value):
    return value[::-1]


values = list(map(reverse_func, sys.stdin.readline().split()))

if int(values[0]) > int(values[1]):
    print(values[0])
else:
    print(values[1])