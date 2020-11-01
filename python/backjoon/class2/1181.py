test_case = int(input())

input_set = set()

for _ in range(0, test_case):
    input_set.add(input())

answer_list = sorted(input_set, key=lambda x: (len(x), x))
for i in range(0, len(answer_list)):
    print(answer_list[i])
