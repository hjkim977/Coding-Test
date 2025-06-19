n = int(input())
result = [] # 감소하는 수를 저장

def backtrack(num,last): # 감소 : 뒤에 붙는 숫자가 앞에 수보다 작음
    result.append(num)
    for next in range(last):
        backtrack(num*10+next, next) # *10인 이유 : 현재 숫자 뒤에 하나의 숫자를 붙이는거니까

for i in range(10):
    backtrack(i,i)

result.sort()

if n<len(result):
    print(result[n])
else:
    print(-1) 