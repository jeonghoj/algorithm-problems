from collections import deque
import sys

command_list = dict()
command_list['push_front'] = 0
command_list['push_back'] = 1
command_list['pop_front'] = 2
command_list['pop_back'] = 3
command_list['size'] = 4
command_list['empty'] = 5
command_list['front'] = 6
command_list['back'] = 7

dq = deque()


def deque_command(com, n):
    if com == 0:
        dq.appendleft(n)
    elif com == 1:
        dq.append(n)
    elif com == 2:
        print(dq.popleft() if len(dq) != 0 else -1)
    elif com == 3:
        print(dq.pop() if len(dq) != 0 else -1)
    elif com == 4:
        print(len(dq))
    elif com == 5:
        print(1 if len(dq) == 0 else 0)
    elif com == 6:
        print(dq[0] if len(dq) != 0 else -1)
    elif com == 7:
        print(dq[len(dq) - 1] if len(dq) != 0 else -1)


test_case = int(input())

for _ in range(test_case):
    input_str = list(sys.stdin.readline().strip('\n').split(' '))
    if len(input_str) > 1:
        command = input_str[0]
        num = input_str[1]
    else:
        command = input_str[0]
        num = None
    deque_command(command_list[command], num)
