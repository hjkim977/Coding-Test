# [Bronze IV] 숫자의 합 - 11720 

[문제 링크](https://www.acmicpc.net/problem/11720) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

구현, 수학, 문자열

### 제출 일자

2024년 8월 19일 17:08:13

### 문제 설명

<p>N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.</p>

### 출력 

 <p>입력으로 주어진 숫자 N개의 합을 출력한다.</p>

### 💡 내 풀이
- 둘째줄에 입력 받은 값을 리스트 형태로 변환 후에 각 자리를 합하는 방식으로 풀었음
- 방법1
```python
a=int(input())
b=list(input())
sum = 0

for i in range(a):
   s = int(b[i])
   sum += s
print(sum)
```
- 방법2
```python
a=int(input())
num=map(int, input())
num=list(num)
sum=sum(num)
print(sum)
```
![image](https://github.com/user-attachments/assets/e677b9c2-e679-4047-8408-1518fa0215f6)

방법2가 메모리, 시간, 코드 길이가 더 짧다. 

