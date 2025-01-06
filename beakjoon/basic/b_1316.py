import sys


def is_group_word(word):
    unique_chars = ''.join(dict.fromkeys(word))

    index = 0
    for char in list(word):
        if char == unique_chars[index]:
            continue
        elif len(unique_chars) > index + 1 and char == unique_chars[index + 1]:
            index += 1
        else:
            return False

    return True


num = int(sys.stdin.readline().strip())
result = 0

for i in range(num):
    word = sys.stdin.readline().strip()
    if is_group_word(word):
        result += 1

print(result)
