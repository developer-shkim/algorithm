import sys

dividend, order = map(int, sys.stdin.readline().split())

divisor = 1
count = 0

while True:
    if dividend % divisor == 0:
        count += 1

    if count == order:
        print(divisor)
        break

    if dividend == divisor:
        print(0)
        break

    divisor += 1
