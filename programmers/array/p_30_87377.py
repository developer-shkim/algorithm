from itertools import combinations


def solve_equations(equations):
    result = []
    for combo in combinations(equations, 2):
        a = combo[0]
        b = combo[1]

        if (a[0] * b[1] - a[1] * b[0]) == 0:
            continue

        x = (a[1] * b[2] - a[2] * b[1]) / (a[0] * b[1] - a[1] * b[0])
        y = (a[2] * b[0] - a[0] * b[2]) / (a[0] * b[1] - a[1] * b[0])

        if not (x.is_integer() and y.is_integer()):
            continue

        result.append((x, y))
    return result


def get_intersection_list(points):
    min_x, max_x = min(point[0] for point in points), max(point[0] for point in points)
    min_y, max_y = min(point[1] for point in points), max(point[1] for point in points)

    cols, rows = int(max_x - min_x + 1), int(max_y - min_y + 1)

    grid = [['.'] * cols for _ in range(rows)]

    for point in points:
        y = 0 if point[0] == min_x else int(abs(min_x - point[0]))
        x = 0 if point[1] == max_y else int(abs(max_y - point[1]))

        grid[x][y] = "*"

    return [''.join(row) for row in grid]


def solution(line):
    points = solve_equations(line)
    answer = get_intersection_list(points)

    return answer


assert solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]) == ["....*....", ".........",
                                                                                     ".........", "*.......*",
                                                                                     ".........", ".........",
                                                                                     ".........",
                                                                                     ".........",
                                                                                     "*.......*"]
assert solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]) == ["*.*"]
assert solution([[1, -1, 0], [2, -1, 0]]) == ["*"]
assert solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]) == ["*"]
