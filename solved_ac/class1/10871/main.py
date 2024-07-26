n,x = map(int, input().split(' '))

sequence = list(map(int, input().split(' ')))

answer = list()
for i in range(n):
    if sequence[i] < x:
        answer.append(sequence[i])

for i in range(len(answer)):
    print(answer[i], end=' ')
