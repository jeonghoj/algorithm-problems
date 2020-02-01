def solution(budgets, M):
	answer = 0
	limit = M // len(budgets)
	max_limit = max(budgets)

	sum_max = 0
	while limit < max_limit:
		sum_temp = 0
		for v in budgets:
			sum_temp = sum_temp + (limit if v > limit else v)

		if M > sum_temp > sum_max:
			sum_max = sum_temp
			answer = limit

		limit = limit + 1

	return answer


budget = [120, 110, 140, 150]
M = 485
# answer 127
print(solution(budget, M))
