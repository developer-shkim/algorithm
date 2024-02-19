import sys

count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

assert count == len(numbers)

print(min(numbers), max(numbers))


