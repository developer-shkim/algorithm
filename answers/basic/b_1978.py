import sys
import math


def is_prime_number(x):
    if x == 1:
        return False

    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            return False
    return True


count = int(sys.stdin.readline().strip())
result = 0

input_numbers = list(map(int, sys.stdin.readline().split()))

for i in range(0, count):
    if is_prime_number(input_numbers[i]):
        result += 1


print(result)
