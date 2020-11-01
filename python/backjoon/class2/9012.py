test_case = int(input())

input_list = []
for _ in range(test_case):
    input_list.append(list(input()))

# ps (Parenthesis String)
for ps in input_list:
    flag = 0
    stack = []
    for v in ps:
        if v == '(':
            stack.append(v)
        elif v == ')':
            if len(stack) == 0:
                flag = 1
                print('NO')
                break
            else:
                stack.pop()

    # print(stack)
    # print(len(stack))
    if len(stack) > 0:
        print('NO')
    elif flag == 1:
        continue
    else:
        print('YES')
