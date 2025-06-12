n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
visited = [False]*n

min_result = float('inf')

def team_score(team):
    score=0
    for i in team:
        for j in team:
            score+=s[i][j]
    return score

def backtrack(idx, count):
    global min_result
    
    # 1. 팀 만들기
    if count==n//2:
        team1 = []
        team2 = []
        for i in range(n):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)

        # 2. 능력치 계산
        score1 = team_score(team1)
        score2 = team_score(team2)
        min_result = min(min_result, abs(score1-score2))
        return

    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            backtrack(i+1, count+1)
            visited[i]=False

backtrack(0,0)
print(min_result)