def solution(phone_book):
    answer = True
    for index,prefix in enumerate(phone_book):
        if answer is False :
            break

        temp_num_array = phone_book[:]
        temp_num_array.pop(index)
        for number in temp_num_array:
            if len(prefix) > len(number):
                continue
            else:
                sliced_number = number[:len(prefix)]
                if sliced_number == prefix:
                    answer = False
                    break

    return answer