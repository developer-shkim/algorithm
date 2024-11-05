import sys

value, number_format = map(int, sys.stdin.readline().strip().split())

result_length = 0
value_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 알파벳을 숫자로 변환

while value >= int(number_format) ** result_length:
    result_length += 1

result = ''

for index in range(result_length - 1, -1, -1):
    position_value = number_format ** index
    result += str(value_list[value // position_value])
    value = value - (value // position_value * position_value)

print(result)
