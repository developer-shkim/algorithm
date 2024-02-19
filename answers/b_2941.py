import sys

word = sys.stdin.readline().strip()
translators = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in translators:
    word = word.replace(char, ' ')

print(len(word))
