import sys

n, k = map(int, sys.stdin.readline().split())

people_list = [i + 1 for i in range(n)]

answer_list = []


def jose(left_people, index, last_index):
    next_index = last_index + len(left_people)
    kill_list = []
    while index - 1 - last_index < len(left_people):
        if index % k == 0:
            kill_list.append(index - 1 - last_index)

        index += 1

    for i, v in enumerate(kill_list):
        answer_list.append(left_people.pop(v - i))

    if len(left_people) < k:
        for v in left_people:
            answer_list.append(v)
    else:
        jose(left_people, index, next_index)


jose(people_list, 1, 0)

print('<', end='')
print(', '.join(map(str, answer_list)), end='')
print('>', end='')
