import sys

target = int(sys.stdin.readline().strip())
turn = 1
start = 2

while start <= target:
    start += 6 * turn
    turn += 1

print(turn)
