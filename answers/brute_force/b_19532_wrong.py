import sys

# 부동소수점 문제로 틀린 결과 출력됨
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (c - ((b * f) / e)) / (a - ((b * d) / e))
y = (c - ((a * f) / d)) / (b - ((a * e) / d))

print(int(x), int(y))
