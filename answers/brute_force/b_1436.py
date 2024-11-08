from sys import stdin

END_OF_NUMBER = '666'


def next_end_of_number(current):
    result = current + 1
    while END_OF_NUMBER not in str(result):
        result += 1

    return result


def find_nth_end_of_number(n):
    if n == 1:
        return int(END_OF_NUMBER)

    result = int(END_OF_NUMBER)
    for i in range(2, n + 1):
        result = next_end_of_number(result)

    return result


print(find_nth_end_of_number(int(stdin.readline().strip())))
