# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 2, 1]
# 두개의 포인터를 이용
start_pointer = 0
last_pointer = len(height) - 1

max_area = 0

# 두개의 포인터가 교차할때까지
while start_pointer > last_pointer:
    # 높이가 낮은것 * 포인터 사이의 거리
    max(max_area, min(height[start_pointer], height[last_pointer]) * abs(start_pointer - last_pointer))

    # 포인터 이동

    # 포인터가 이동할 시, x가 줄어드는데에 따른 y 길이를 최대화 하기 위해,
    # y가 최대인 쪽을 유지하여 너비 최대화
    # 높이가 낮은 쪽의 포인터를 이동
    if height[start_pointer] > height[last_pointer]:
        last_pointer += 1
    else:
        start_pointer += 1


