import sys

T = int(sys.stdin.readline())
results = []

for i in range(T):
    R, S = sys.stdin.readline().split()
    results.append(''.join(j*int(R) for j in S))

print(*results, sep='\n')

