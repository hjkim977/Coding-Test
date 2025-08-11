k = int(input())
signs = list(input().split())
visited = [0]*10 # 0~9까지 사용했는지 확인하는 배열
answer = []

def check(a,b,sign):
    if sign == '<':
        return a<b
    else:
        return a>b

def dfs(cnt,num):
    if cnt==k+1: # 숫자 개수가 k+1이면 answer에 추가
        answer.append(num)
        return
    
    for i in range(10): # i는 추가하려는 수
        if not visited[i]:
            if cnt==0 or check(num[-1],str(i),signs[cnt-1]):
                visited[i]=1
                dfs(cnt+1, num+str(i))
                visited[i]=0

dfs(0,"")
print(max(answer))
print(min(answer))