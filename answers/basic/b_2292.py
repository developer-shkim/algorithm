import sys

target = int(sys.stdin.readline().strip())
turn = 1
start = 2
end = 7

if target != 1:
    while not start <= target <= end:
        start += 6 * turn
        end += 6 * (turn + 1)
        turn += 1

print(turn if target == 1 else turn + 1)