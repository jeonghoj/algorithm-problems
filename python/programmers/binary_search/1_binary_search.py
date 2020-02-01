def solution(budgets, M):
	answer = 0

	min_range = 0
	max_range = max(budgets)
	while min_range <= max_range:
		print("min", min_range)
		print("max", max_range)
		sum_temp = 0
		limit = min_range + ((max_range - min_range) // 2)
		for v in budgets:
			sum_temp = sum_temp + (limit if v > limit else v)

		if sum_temp > M:
			max_range = limit - 1
		else:
			answer = max(limit, answer)
			min_range = limit + 1

	return answer


budgets = [120, 110, 140, 150]
M = 485

# solution 127

print(solution(budgets, M))
