import sys

n,m=list(map(int,sys.stdin.readline().split()))
brand=[]
price=0

for _ in range(m):
    p,i=list(map(int,sys.stdin.readline().split()))
    brand.append((p,i))

best_p=min(brand, key=lambda x:x[0])[0]
best_i=min(brand, key=lambda x:x[1])[1]

if best_p > best_i*6: #18 > 12
    price=n*best_i

else:
    price=(n//6)*best_p+min(best_p,best_i*(n%6))

print(price)