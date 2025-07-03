n,c = list(map(int,input().split()))
house = list(int(input()) for _ in range(n))

house.sort()

left = 1 #최소
right = house[-1]-house[0] #최대
result = 0

def distance(left, right):
    global result
    while left<=right:
        mid = (left+right)//2 # 공유기 간 최소 거리 후보
        current = house[0]
        cnt = 1 # 설치한 공유기 수

        for i in range(1,n):
            if house[i]-current >= mid:
                cnt+=1
                current = house[i]
        if cnt >=c:
            result = mid
            left = mid +1
        else:
            right = mid -1

distance(left,right)
print(result)