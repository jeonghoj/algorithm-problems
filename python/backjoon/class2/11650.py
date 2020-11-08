test_case = int(input())

input_list = []
for i in range(test_case):
    input_list.append(tuple(map(int, input().split())))

for v in sorted(input_list, key=lambda x: (x[0], x[1])):
    print(v[0], v[1])
