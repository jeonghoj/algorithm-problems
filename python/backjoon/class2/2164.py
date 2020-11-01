from collections import deque

input_num = int(input())

input_deque = deque([x for x in range(1, input_num + 1)])


for _ in range(input_num):
    if len(input_deque) == 1:
        print(input_deque.popleft())
        break
    else:
        input_deque.popleft()
        input_deque.append(input_deque.popleft())