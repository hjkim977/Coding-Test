n = int(input())
k = int(input())
s = [int(input()) for _ in range(n)]
visited = [False]*n
cards = set()

def backtrack(num):
    if len(num)==k:
        cards.add(''.join(map(str,num)))
        return

    for i in range(len(s)):
        if not visited[i]:
            visited[i] = True
            backtrack(num+[s[i]])
            visited[i] = False

backtrack([])
print(len(cards))