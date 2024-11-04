import sys


def fn(a1, n0, a0):
    return a1 * n0 + a0


def gn(c, n0):
    return c * n0


def check(a1, a0, c, n0):
    return int(fn(a1, n0, a0) <= gn(c, n0) and a1 <= c)


input_a, input_b = map(int, sys.stdin.readline().split())
input_c = int(sys.stdin.readline().strip())
input_x = int(sys.stdin.readline().strip())

print(check(input_a, input_b, input_c, input_x))
