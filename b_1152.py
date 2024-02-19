import sys

sentence = sys.stdin.readline().strip()
countOfWords = 0

if len(sentence) > 0:
    countOfWords = sentence.count(' ') + 1

print(countOfWords)