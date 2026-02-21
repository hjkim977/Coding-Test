import sys
input=sys.stdin.readline
n1=int(input())
cards1=set(map(int, input().split()))

n2=int(input())
cards2=list(map(int, input().split()))

for card in cards2:
    if card in cards1:
        print(1, end=' ')
    else:
        print(0, end=' ')