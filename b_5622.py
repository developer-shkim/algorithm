import sys

word = sys.stdin.readline().strip()
dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
seconds = 0

for index, dial in enumerate(dials):
    for char in list(word):
        if char in dial:
            seconds += index + 3

print(seconds)
