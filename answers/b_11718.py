inputs = []

while True:
    try:
        sentence = input()
        inputs.append(sentence)
    except EOFError:
        break

print(*inputs, sep='\n', end='')