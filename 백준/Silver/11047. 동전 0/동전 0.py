n,k=map(int,input().split())
coins=[]
count=0

for _ in range(n):
    coins.append(int(input()))

for coin in reversed(coins):
    if k%coin!=k:
        count+=k//coin
        k=k%coin

print(count)