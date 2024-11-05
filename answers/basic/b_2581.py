import sys
import math


def get_min_prime_number(x):
    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            return num
    return x


inputNumber = int(sys.stdin.readline().strip())
target = inputNumber

while target != 1:
    minPrimeNumber = get_min_prime_number(target)
    print(minPrimeNumber)
    target = target // minPrimeNumber

