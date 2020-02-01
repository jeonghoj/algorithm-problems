input_char = "bbbbb"
char_set = set()


def solution():
    answer = 0

    def check_unique(unique_str):
        temp_set = set()
        temp_set.clear()
        list_str = list(unique_str)
        for val in list_str:
            if val in temp_set:
                return False
            temp_set.add(val)

        return True

    for i in range(len(input_char)):
        for j in range(len(input_char) - i):
            if check_unique(input_char[i:i + j + 1]):
                answer = max(answer, (i+j+1) - i)

    print(answer)


solution()
