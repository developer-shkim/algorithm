from sys import stdin

input_arr = [int(stdin.readline().strip()) for _ in range(int(stdin.readline().strip()))]
input_arr.sort()
print(*input_arr, sep='\n')
