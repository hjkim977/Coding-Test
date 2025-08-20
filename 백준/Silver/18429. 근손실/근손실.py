from itertools import permutations
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
weight_rise = list(map(int,input().split()))
weight_num = []
cnt = 0

for i in range(n):
    weight_num.append(i)
seq = list(permutations(weight_num,n))

for i in range(len(seq)):
    weight = 500
    v = True
    for j in range(len(seq[0])):
        index = seq[i][j]
        weight+=weight_rise[index]-k
        if weight<500:
            v = False
            break
    if v:
        cnt+=1

print(cnt)