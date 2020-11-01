white_first_list = []
for _ in range(0, 8):
    if _ % 2 == 0:
        white_first_list.append(list('WBWBWBWB'))
    else:
        white_first_list.append(list('BWBWBWBW'))

black_first_list = []
for _ in range(0, 8):
    if _ % 2 == 0:
        black_first_list.append(list('BWBWBWBW'))
    else:
        black_first_list.append(list('WBWBWBWB'))

n, m = map(int, input().split())

input_list = []

for _ in range(0, n):
    input_list.append(list(input()))

answer = m * n
for x in range(0, n - 7):
    for y in range(0, m - 7):
        count = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if input_list[x + i][y + j] != white_first_list[i][j]:
                    count += 1
        answer = min(count, answer)
        count = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if input_list[x + i][y + j] != black_first_list[i][j]:
                    count += 1
        answer = min(count, answer)

print(answer)
