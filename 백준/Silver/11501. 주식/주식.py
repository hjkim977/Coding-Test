t=int(input())
for i in range(t):
    n=int(input())
    stock=list(map(int, input().split()))
    
    profit=0
    max=0

    for j in range(n-1,-1,-1): # n-1부터 0까지 역순으로 반복
        if stock[j]> max:
            max=stock[j]
        profit+=max-stock[j]
    print(profit)