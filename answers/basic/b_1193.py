import sys

number = int(sys.stdin.readline().strip()) - 1

start = 0
end = 0
orderByAsc = False
roundNumber = 1

while not (start <= number <= end):
    start += 1 + (roundNumber - 1)
    end += 2 + (roundNumber - 1)
    orderByAsc = not orderByAsc
    roundNumber += 1

values = list(range(start, end + 1))

if orderByAsc:
    numerator = values.index(number) + 1
    denominator = values[::-1].index(number) + 1
    print("%d/%d" % (numerator, denominator))
else:
    numerator = values[::-1].index(number) + 1
    denominator = values.index(number) + 1
    print("%d/%d" % (numerator, denominator))

# if not orderByAsc:
#     print(''.join(map(str, (values.index(number), values[::-1].index(number)))[::-1]))
# else:
#     print(''.join(map(str, (values.index(number), values[::-1].index(number)))[::1]))

'''
분수는 각 행,열 인덱스에 +1 하면 됨
각 대각선은 행, 열의 합이 같음
대각선의 합은 0, 1, 2, 3.. 으로 증가함
대각선 기준으로 오름차순, 내림차순을 설정할 수 있는 flag

sum = 0

0   0   1   2   1   0   0   1   2   3   4   3   2   1   0   "0, 01, 210, 0123, 43210, 012345
0   1   0   0   1   2   3   2   1   0   0   1   2   3   4   "0, 10, 012, 3210, 01234, 543210
00  01  10  20  11  02  03  12  21  30  40  31  22  13  04


        d   a   d     a      d   
        0, 1-2, 3-5, 6-9, 10-14
        0   1   2     3      4
start   0   1   3     6    10
end     0   2   5     9    14
'''
