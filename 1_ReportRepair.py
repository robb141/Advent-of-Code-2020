input_list = [int(i) for i in open('1.txt').read().splitlines()]

ln_list = len(input_list)

for i in range(ln_list):
    for j in range(i + 1, ln_list):
        for k in range(j + 1, ln_list):
            if input_list[i] + input_list[j] + input_list[k] == 2020:
                print(input_list[i] * input_list[j] * input_list[k])

