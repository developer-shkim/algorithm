import sys

numbers = [int(sys.stdin.readline()) for _ in range(9)]
maxValue = max(numbers)

print(maxValue)
print(numbers.index(maxValue) + 1)


