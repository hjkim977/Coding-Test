n=int(input())
p=list(map(int,input().split()))
delete_n=int(input())

root=0
tree=[[] for _ in range(n)]

for child,parent in enumerate(p):
    if parent==-1:
        root=child
    else:
        tree[parent].append(child)

def dfs(node):
    if node==delete_n:
        return 0
    
    if not tree[node]:
        return 1
    leaf_count=0
    for child in tree[node]:
        leaf_count+=dfs(child)
    if leaf_count==0:
        return 1
    return leaf_count

if root==delete_n:
    print(0)
else:
    print(dfs(root))