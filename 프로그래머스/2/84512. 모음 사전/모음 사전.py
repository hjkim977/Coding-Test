def solution(word):
    words = []
    alp = ['A','E','I','O','U']
    def dfs(cnt,w):
        if cnt==5:
            return
        for i in alp:
            words.append(w+i)
            dfs(cnt+1,w+i)
    dfs(0,"")
    return words.index(word)+1