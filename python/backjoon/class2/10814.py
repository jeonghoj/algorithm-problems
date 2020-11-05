import operator

test_case = int(input())

input_list = []
for i in range(test_case):
    user = dict()
    user['age'], user['name'] = input().split()
    user['index'] = i
    input_list.append(user)

for v in sorted(input_list, key=lambda x: (int(x['age']), int(x['index']))):
    print(v['age'], v['name'])
