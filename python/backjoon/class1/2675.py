test_case = int(input())
input_list = []
for _ in range(0, test_case):
    input_list.append(input().split(' '))

for i in range(0, test_case):
    string = list(input_list[i][1])
    for j in range(0, len(string)):
        for _ in range(0, int(input_list[i][0])):
            print(string[j], end='')

    print()
