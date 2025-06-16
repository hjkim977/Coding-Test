def backtrack(start, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return

    for i in range(start, len(s)):
        backtrack(i+1, lotto+[s[i]])

while True:
    t = list(map(int,input().split()))
    if t[0] == 0:
        break
    s = t[1:]
    backtrack(0, [])
    print()