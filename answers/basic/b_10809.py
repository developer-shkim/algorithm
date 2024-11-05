import sys

word = sys.stdin.readline().strip()

for i in range(ord('a'), ord('z')+1):
    index = word.find(chr(i))
    print(index, end='')
