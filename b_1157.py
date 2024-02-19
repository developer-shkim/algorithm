import sys

word = sys.stdin.readline().strip()
upperWord = word.upper()

firstPrizeChar = ''
firstPrizeCharCount = 0
secondPrizeCharCount = 0

for char in ''.join(set(upperWord)):
    if upperWord.count(char) > firstPrizeCharCount:
        firstPrizeChar = char
        firstPrizeCharCount = upperWord.count(char)

    elif upperWord.count(char) > secondPrizeCharCount:
        secondPrizeCharCount = upperWord.count(char)

if firstPrizeCharCount == secondPrizeCharCount:
    print('?')
else:
    print(firstPrizeChar)


