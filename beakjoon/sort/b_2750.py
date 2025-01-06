from sys import stdin

arr = [int(stdin.readline().strip()) for _ in range(int(input()))]

for i in range(0, len(arr)):
    target = min(arr)
    print(target)

    arr.pop(arr.index(target))
