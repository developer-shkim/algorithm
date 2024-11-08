import sys
from sys import stdin


def solve():
    rows, cols = map(int, stdin.readline().split())
    tiles = []

    for i in range(0, rows):
        tiles.append(list(stdin.readline().strip()))

    print(get_repainted_tiles(tiles, cols, rows))


def get_repainted_tiles(tiles, cols, rows):
    result = sys.maxsize
    for col in range(0, cols - 7):
        for row in range(0, rows - 7):
            result = min(result, find_differences_by_tile(tiles, col, row))

    return result


def find_differences_by_tile(tiles, col_start, row_start):
    answers = [
        [
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB'
        ],
        [
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
        ]
    ]

    result1 = 0
    result2 = 0

    for row in range(row_start, row_start + 8):
        result1 += find_differences_by_row(tiles[row][col_start: col_start + 8], answers[0][row - row_start])
        result2 += find_differences_by_row(tiles[row][col_start: col_start + 8], answers[1][row - row_start])
    return min(result1, result2)


def find_differences_by_row(str1, str2):
    differences = sum(1 for a, b in zip(str1, str2) if a != b)
    return differences


solve()
