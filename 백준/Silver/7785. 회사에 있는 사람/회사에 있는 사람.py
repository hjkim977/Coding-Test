n=int(input())
log=set()
for _ in range(n):
    a,b=input().split()
    if b=="enter":
        log.add(a)
    elif b=="leave":
        log.remove(a)
log=sorted(log,reverse=True)
print('\n'.join(log))