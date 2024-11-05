import sys

n, m = map(int, sys.stdin.readline().split())

inputs = []
results = []

for i in range(n):
    inputs += list(map(int, sys.stdin.readline().split()))

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in range(m):
        results.append(inputs[i * m + j] + temp[j])


for i in range(n):
    print(*results[i * m:(i+1)*m])
