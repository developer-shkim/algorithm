import sys

count = int(sys.stdin.readline().strip())
coins = [25, 10, 5, 1]
result = []

for i in range(count):
    money = int(sys.stdin.readline())
    money_result = []

    for coin in coins:
        coin_count = money // coin
        money_result.append(coin_count)
        money = money % coin

    result.append(money_result)

for row in result:
    print(*row)