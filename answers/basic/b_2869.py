import sys
import math

day, night, goal = map(int, sys.stdin.readline().split())

if day >= goal:
    print(1)
else:
    print(math.ceil((goal - day) / (day - night)) + 1)