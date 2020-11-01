num = int(input())

input_list = list(map(int, input().split()))

count = 0
for v in input_list:
    flag = 0
    if v == 1:
        continue
    for i in range(2, v):
        if v % i == 0:
            flag = 1
            break

    if flag != 1:
        count += 1

print(count)
