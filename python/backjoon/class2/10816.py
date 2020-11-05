import sys

hand_len = int(sys.stdin.readline())
hand_list = list(sys.stdin.readline().split())

hand_dict = dict()
for v in hand_list:
    if v in hand_dict:
        hand_dict[v] += 1
    else:
        hand_dict[v] = 1

q_len = int(sys.stdin.readline())
q_list = list(sys.stdin.readline().split())

for i in range(q_len):
    if q_list[i] in hand_dict:
        print(hand_dict[q_list[i]], end='')
    else:
        print(0, end='')

    if i != q_len-1:
        print(end=' ')
