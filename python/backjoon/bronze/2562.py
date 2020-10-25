input_list = []

for _ in range(0, 9):
    input_list.append(int(input()))

original_list = input_list.copy()
input_list.sort()

print(input_list[-1])
print(original_list.index(input_list[-1], 0, len(input_list))+1)
