test_case = int(input())

for _ in range(test_case):
    h, w, n = map(int, input().split())

    yy = n % h
    if yy == 0:
        yy = 1

    xx = n // h
    if xx % 2 == 0 or (xx+1) % 2 == 0:
        xx = xx + 1
    else:
        xx = xx

    print(int('{0}{1:02}'.format(yy, xx)))
