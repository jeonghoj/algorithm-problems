n = int(input())

n_set = set()
for v in list(map(int, input().split())):
    n_set.add(v)

m = int(input())
input_list = map(int, (input().split()))

for v in input_list:
    if v in n_set:
        print(1)
    else:
        print(0)
