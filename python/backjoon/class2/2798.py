from itertools import combinations

n, m = map(int, input().split())

input_list = list(map(int, input().split()))

min_difference = None
best_answer = None
for v in list(combinations(input_list, 3)):
    if min_difference is None:
        min_difference = abs(m - sum(v))
    elif sum(v) <= m and (m-sum(v) < min_difference):
        min_difference = m - sum(v)
        best_answer = sum(v)

print(best_answer)
