import sys


def get_value_count_is_1(key_counts):
    return list(filter(lambda x: key_counts[x] == 1, key_counts))[0]


number_map_list = [map(int, sys.stdin.readline().split()) for _ in range(3)]
x_key_counts = {}
y_key_counts = {}

for number_map in number_map_list:
    x, y = number_map
    if x in x_key_counts:
        x_key_counts[x] += 1
    else:
        x_key_counts[x] = 1

    if y in y_key_counts:
        y_key_counts[y] += 1
    else:
        y_key_counts[y] = 1

print(get_value_count_is_1(x_key_counts), get_value_count_is_1(y_key_counts))
