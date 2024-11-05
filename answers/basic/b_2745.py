import sys


def is_alphabet(param):
    return 65 <= ord(param) <= 90


number, number_format = sys.stdin.readline().strip().split()

result = 0

for index, value in enumerate(list(number)):
    if is_alphabet(value):
        result += (ord(value) - 55) * int(number_format) ** (len(number) - 1 - index)

    else:
        result += int(value) * int(number_format) ** (len(number) - 1 - index)

print(result)
