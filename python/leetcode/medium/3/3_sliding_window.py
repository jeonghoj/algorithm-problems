def solution():
	input_char = "bbbbb"
	answer = 0

	char_set = set()

	i = j = 0

	while i < len(input_char) and j < len(input_char):

		if input_char[j] not in char_set:
			char_set.add(input_char[j])
			j = j + 1
			answer = max(answer, j - i)
		else:
			char_set.remove(input_char[i])
			i = i + 1

	print(answer)


solution()
