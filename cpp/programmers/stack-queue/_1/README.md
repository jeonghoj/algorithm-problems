REVIEW

풀면서 계속

(signal: segmentation fault (core dumped))

(signal: aborted (core dumped))

오류가 났었는데 이는 queue 범위를 넘어갔을때 발생하는 오류이다.
즉 size가 0인데 계속 호출한다던지..

재귀를 통해 체크하는 함수에서 queue의 size 체크를 하지않아 계속 오류가 발생했다.

경계값, 빈값 체크하는 걸 꼼꼼히 하자 -_-