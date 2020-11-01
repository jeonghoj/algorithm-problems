white_first_list = []
for i in range(0, 8):
    if i % 2 == 0:
        white_first_list.append(list('WBWBWBWB'))
    else:
        white_first_list.append(list('BWBWBWBW'))

black_first_list = []
for i in range(0, 8):
    if i % 2 == 0:
        black_first_list.append(list('BWBWBWBW'))
    else:
        black_first_list.append(list('WBWBWBWB'))

n, m = map(int, input().split())

input_list = []

for _ in range(0, n):
    input_list.append(list(input()))


def paint(y, x):
    count = 0

    if input_list[x][y] == 'W':
        for i in range(0, 8):
            for j in range(0, 8):
                if input_list[x + i][y + j] != white_first_list[i][j]:
                    count += 1
    else:
        for i in range(0, 8):
            for j in range(0, 8):
                if input_list[x + i][y + j] != black_first_list[i][j]:
                    count += 1
    return count


# 초기값
answer = m * n
for i in range(0, n - 8):
    for j in range(0, m - 8):
        answer = min(answer, paint(j, i))

print(answer)
