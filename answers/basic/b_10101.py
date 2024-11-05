import sys

angles = [int(sys.stdin.readline().strip()) for _ in range(3)]
triangles = ['Equilateral', 'Isosceles', 'Scalene']

if sum(angles) == 180:
    print(triangles[len(set(angles)) - 1])
else:
    print('Error')
