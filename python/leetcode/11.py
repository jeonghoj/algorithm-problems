# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 2, 1]
max_area_list = []

start_pointer = 0
last_pointer = len(height) - 1

while start_pointer != last_pointer:
    if height[start_pointer] >= height[last_pointer]:
        print(height[last_pointer], (abs(start_pointer - last_pointer)))
        max_area_list.append(height[last_pointer] * (abs(start_pointer - last_pointer)))
        last_pointer -= 1
    else:
        print(height[last_pointer], (abs(start_pointer - last_pointer)))
        max_area_list.append(height[start_pointer] * (abs(start_pointer - last_pointer)))
        start_pointer += 1

print(max_area_list)
print(max(max_area_list))
