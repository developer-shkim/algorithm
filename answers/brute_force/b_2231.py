import sys


def find_constructor(target):
    if target < 10:
        return target // 2 if target % 2 == 0 else 0

    constructor = max(1, target - 9 * len(str(target)))

    while constructor != target:
        nums = [int(split) for split in str(constructor)]
        if constructor + sum(nums) == target:
            return constructor

        constructor += 1

    return 0


n = int(sys.stdin.readline().strip())
print(find_constructor(n))

