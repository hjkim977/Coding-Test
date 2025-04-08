n=int(input())
word=[input() for _ in range(n)] #입력 받는 단어를 word 리스트에 저장
r={} #뒤집어진 문자열

for i in word:
    r[i]=i[::-1]

for value in r.values():
    if value in word:
        print(len(value),value[len(value)//2])
        break