test_case = int(input())

answer_list = []
for _ in range(test_case):
    h, w, n = map(int, input().split())

    yy = n % h

    xx = n // h + 1
    if yy == 0: yy = h;xx -= 1
    print(yy * 100 + xx)
