출처 : https://codeup.kr/problem.php?id=1019

Java String 클래스의 split 함수를 사용하였다.  
split은 문자열 배열(String[])을 return한다.  
regex로 나누기 때문에 "."은 오류를 일으킨다. Regex에서 .은 모든 글자를 의미한다.  
따라서 \\. 으로 처리해준다.  

테스트 케이스 오류
0099.01.01

년도도 똑같이 포맷 처리해준다.

---

%04d

- 4칸을 채워라 
- 빈칸은 0으로
- 숫자형으로 출력