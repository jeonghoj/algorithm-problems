test_case = int(input())

q_list = []

for _ in range(0, test_case):
    q_list.append(input())

final_score = 0
for i in range(0, test_case):

    score = 0
    for v in list(q_list[i]):
        if v == 'O':
            score += 1
        elif v == 'X':
            score = 0
        final_score += score

    print(final_score)
    final_score = 0
