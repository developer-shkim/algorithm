import sys

number, number_format = sys.stdin.readline().strip().split()

result = 0
value_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 알파벳을 숫자로 변환

for index, value in enumerate(list(number)):
    result += int(value_list.index(value)) * int(number_format) ** (len(number) - 1 - index)

print(result)
