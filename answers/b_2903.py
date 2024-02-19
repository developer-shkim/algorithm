import sys
import math

count = int(sys.stdin.readline().strip())

print(int(math.pow(math.pow(2, count) + 1, 2)))

'''
1) 9 = 3^2 (4 2^2 = 2^1^1)
2) 25 = 5^2 (16 4^2 = 2^2^2)
3) 81 = 9^2 (64 8^2 = 2^3^2) 
4) 289 = 17^2 (256 16^2 = 2^4^2) 
5) 1089 = 33^2 (1024 32^2 = 2^5^2)

'''


