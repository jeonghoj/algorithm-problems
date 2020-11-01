import sys
test_case = int(sys.stdin.readline())

input_list = []
for _ in range(test_case):
    input_list.append(int(sys.stdin.readline()))

for v in sorted(input_list):
    print(v)
