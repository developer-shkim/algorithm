import sys

count = int(sys.stdin.readline().strip())

for i in range(1, count):
    print(" " * (count - i), "*" * (i + (i - 1)), sep="")

for i in range(count, 0, -1):
    print(" " * (count - i), "*" * (i + (i - 1)), sep="")
