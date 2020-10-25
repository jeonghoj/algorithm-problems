input_list = input().split()

flag = 0
back = 0
for i, v in enumerate(input_list):
    if flag == 0:
        if input_list[0] < input_list[1]:
            flag = 'ascending'
        else:
            flag = 'descending'

    elif flag == 'ascending':
        if back > v:
            flag = 'mixed'
            break
    elif flag == 'descending':
        if back < v:
            flag = 'mixed'
            break

    back = v

print(flag)
