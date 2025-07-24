def solution(N, number):
    if N==number:
        return 1
    
    answer = -1
    arr = [set() for _ in range(8)] #8보다 크면 -1 return이니까
    
    for i in range(len(arr)):
        arr[i].add(int(str(N)*(i+1)))
        # 숫자만큼 n이 붙어서 저장됨
    
    for i in range(1,8): #{55}부터 연산이 들어갈 수 있기 때문에 1부터 시작
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i-j-1]:
                    arr[i].add(op1+op2)
                    arr[i].add(op1-op2)
                    arr[i].add(op1*op2)
                    if op2!=0: #0으로는 나눌 수 없으니까
                        arr[i].add(op1//op2) #나머지는 무시하라고 했으니까
                        
        if number in arr[i]: #매 반복에서 number가 만들어졌는지 확인함
            answer = i+1 #찾았으면 현재 사용횟수 +1하고 종료 => 0부터 저장했기 때문
            break
    return answer