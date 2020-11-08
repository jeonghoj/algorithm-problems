import math,sys
n, k = map(int,sys.stdin.readline().split())
print(math.factorial(n)//(math.factorial(n-k)*math.factorial(k)))