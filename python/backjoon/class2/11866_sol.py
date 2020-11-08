from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
answer_list = []
q = deque()
q = deque([i + 1 for i in range(n)])

while q:
    for i in range(k - 1):
        q.append(q.popleft())
    answer_list.append(q.popleft())

#     for i in range(k):
#         if i == k-1:
#             answer_list.append(q.popleft())
#         else:
#             q.append(q.popleft())
#
# for v in q:
#     answer_list.append(v)
#

# for i, v in enumerate(answer_list):
#     if i != len(answer_list)-1:
#         print(v, end=', ')
#     else:
#         print(v, end='')
#
#
print('<', end='')
print(', '.join(map(str, answer_list)), end='')
print('>', end='')
