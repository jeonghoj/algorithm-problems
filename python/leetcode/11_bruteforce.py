# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 2, 1]
max_area_list = []

# 방문한 곳을 표시한 임시 리스트
temp_height = height[:]
for itr in range(len(height)):
    # 최대값 구하기
    temp_max = max(temp_height)
    # 최대값이 -1이면 모든 곳을 방문했으므로 루프 종료
    if temp_max == -1:
        break

    # 방문한 곳 index 를 임시 저장하고
    temp_max_index = temp_height.index(max(temp_height))
    # 방문했다는 표시로 -1을 할당
    temp_height[temp_max_index] = -1
    # 루프를 돌며 가능한 넓이를 구한다
    for i, x in enumerate(height):
        if x >= temp_max:
            max_area_list.append(temp_max * abs(temp_max_index - i))

print(max_area_list)
print(max(max_area_list))
