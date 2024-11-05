import sys

triangles = ['Equilateral', 'Isosceles', 'Scalene']

while True:
    sides = list(map(int, sys.stdin.readline().strip().split()))

    if len(set(sides)) == 1 and sides[0] == 0:
        break

    if max(sides) >= sum(sides) - max(sides):
        print('Invalid')
        continue

    print(triangles[len(set(sides)) - 1])
