import sys

day, night, goal = map(int, sys.stdin.readline().split())

count = 1
current = 0

while current + day < goal:
    count += 1
    current = current + day - night

print(count)