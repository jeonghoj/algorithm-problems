solution(1) = [0]

solution(2) = [0] + [0] + [1]

solution(3) = [0, 0, 1] + [0] + [0, 1, 1]

solution(4) = [0, 0, 1, 0, 0, 1, 1] + [0] + [0, 0, 1, 1, 0, 1, 1]

solution(n)은

solution(n-1) + [0] + [solution(n-1)의 가운데 항을 1로 바꾼 배열].