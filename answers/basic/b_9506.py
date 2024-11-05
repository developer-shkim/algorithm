import sys


def is_perfect_number(n):
    i = 1
    total = 0
    divisors = []

    while True:
        if total > n:
            return False

        if n == i:
            if total == n:
                return divisors
            else:
                return False

        if n % i == 0:
            divisors.append(i)
            total += i

        i += 1


def print_result(perfect_number, divisors):
    if divisors:
        print("%d = " % perfect_number, end='')
        print(*divisors, sep=' + ')
    else:
        print("%d is NOT perfect." % perfect_number)


while True:
    num = int(sys.stdin.readline().strip())

    if num == -1:
        break

    print_result(num, is_perfect_number(num))

