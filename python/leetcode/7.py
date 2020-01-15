import sys

# inputNum: int = -123
inputNum: int = 1534236469
# int max 2147483647
#         1534236469
# return 0
revNum: int = 0

while inputNum != 0:
    # pop
    pop = inputNum % (10 if inputNum > 0 else -10)
    # input 하고 나눗셈은 int를 반환하도록 명시
    inputNum = int(inputNum / 10)

    # push하기 전 overflow 검사
    ##
    # push 하기 전에 
    # revNum이 (int최대값/최소값)/10 보다 클때거나
    # revNum이 int 최대 최소값 /10 이랑 같은값이면서 최대값의 마지막자리인 7 최소값의 마지막 자리 -8을 넘을때
    # 0을 반환하여 오버플로우임을 알린다
    ##
    print(int((2**31-1)/10))
    print(revNum)
    if revNum > int((2**31-1)/10) or (revNum == sys.maxsize / 10 and pop > 7):
        revNum = 0
        break
    if revNum < int((-2**31)/10) or (revNum == sys.maxsize / 10 and pop < -8):
        revNum = 0
        break

    # push
    revNum = revNum * 10 + pop
    print(revNum)

print(revNum)
