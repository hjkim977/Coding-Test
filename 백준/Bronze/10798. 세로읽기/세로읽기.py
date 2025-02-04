a=[list(input()) for _ in range(5)]
result=[]

for j in range(15):
    for i in range(5):
        if j < len(a[i]):
            result.append(a[i][j])
print("".join(result))