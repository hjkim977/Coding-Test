def solution(n):
    # 0부터 n까지 소수 여부를 저장할 리스트 (일단 모두 True로 초기화)
    ch = [True] * (n + 1)
    answer = 0
    # 0과 1은 소수가 아니므로 제외
    for i in range(2, int(n**0.5) + 1):
        if ch[i] == True: # i가 소수라면
            # i의 배수들은 소수가 아니므로 False로 변경
            for j in range(i*i, n + 1, i):
                ch[j] = False
    
    # True의 개수를 세면 소수의 개수가 나옴 (2부터 n까지)
    for i in range(2, n + 1):
        if ch[i] == True:
            answer+=1
    return answer