n = int(input())
a = list(map(int,input().split()))
visited = [False]*n
nums = []
max_result = -float('inf')

def backtrack(total):
    global max_result

    if len(nums) == n:
        for i in range(len(nums)-1):
            total += abs(nums[i]-nums[i+1])
        max_result = max(total,max_result)
        return

    for i in range(n):
        if not visited[i]:
            nums.append(a[i])
            visited[i]=True
            backtrack(total)
            nums.pop()
            visited[i]=False

backtrack(0)
print(max_result)