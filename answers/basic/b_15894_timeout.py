import sys

bottom_square_count = int(sys.stdin.readline().strip())
square_count = sum(range(1, bottom_square_count + 1))
dotted_t_line_count = sum(range(1, bottom_square_count))

print(square_count * 4 - dotted_t_line_count * 4)
