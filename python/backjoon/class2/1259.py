while True:
    input_str = input()
    if str(input_str) == '0':
        break
    else:
        flag = 0
        if len(input_str) % 2 == 0:
            flag = 0
        else:
            flag = 1
        if input_str[len(input_str) // 2 + flag:] == ''.join(reversed(input_str[:len(input_str) // 2])):
            print('yes')
        else:
            print('no')
