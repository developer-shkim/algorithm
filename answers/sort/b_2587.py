from sys import stdin

count = 5
mid_index = 2
input_numbers = [int(stdin.readline().strip()) for _ in range(0, count)]
mean = int(sum(input_numbers) / count)
median = sorted(input_numbers)[mid_index]

print(mean)
print(median)
