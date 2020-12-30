input = [i for i in open('18.txt').read().splitlines()]

print(input)


def calculate(sentence):
    sentence = sentence.split()
    while '+' in sentence:
        for i in range(len(sentence) - 1, -1, -1):
            if sentence[i] == '+':
                sentence[i-1] = int(sentence[i-1]) + int(sentence[i+1])
                sentence.pop(i)
                sentence.pop(i)
    result = int(sentence[0])
    for i in range(0, len(sentence)):
        if sentence[i] == '*':
            result *= int(sentence[i+1])
    return result


part1 = 0
for inp in input:
    while '(' in inp:
        first_bracket = ''.join(inp).rindex('(')
        for i in range(first_bracket, len(inp)):
            if inp[i] == ')':
                end = i
                break
        temp_inp = inp[first_bracket+1:end].split()
        temp_res = int(temp_inp[0])
        for i in range(0, len(temp_inp)):
            if temp_inp[i] == '+':
                temp_res += int(temp_inp[i+1])
            elif temp_inp[i] == '*':
                temp_res *= int(temp_inp[i+1])
            else:
                pass
        inp = inp[:first_bracket] + str(temp_res) + inp[end+1:]
    inp = inp.split()
    res = int(inp[0])
    for i in range(0, len(inp)):
        if inp[i] == '+':
            res += int(inp[i+1])
        elif inp[i] == '*':
            res *= int(inp[i+1])
        else:
            pass
    part1 += res
print('Part 1:', part1)


part2 = 0
for inp in input:
    while '(' in inp:
        first_bracket = ''.join(inp).rindex('(')
        for i in range(first_bracket, len(inp)):
            if inp[i] == ')':
                end = i
                break
        temp_res = calculate(inp[first_bracket + 1:end])
        inp = inp[:first_bracket] + str(temp_res) + inp[end+1:]
    res = calculate(inp)
    part2 += res
print('Part 2:', part2)
