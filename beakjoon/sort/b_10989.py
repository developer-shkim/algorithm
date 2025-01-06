from sys import stdin


def set_dict(num):
    if num in input_dict.keys():
        input_dict[num] += 1
        return

    input_dict[num] = 1


def print_dict():
    for key in sorted(input_dict.keys()):
        for _ in range(0, input_dict[key]):
            print(key)


n = int(stdin.readline().strip())
input_dict = {}

for _ in range(0, n):
    set_dict(int(stdin.readline().strip()))

print_dict()
