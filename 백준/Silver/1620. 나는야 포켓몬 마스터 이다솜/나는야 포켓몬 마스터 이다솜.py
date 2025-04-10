n, m = map(int, input().split())
key_name = {}
key_num = {}

for i in range(1, n + 1):
    a = input()
    key_name[a] = i
    key_num[i] = a

result = []
for _ in range(m):
    q = input()
    if q.isdigit():
        result.append(key_num[int(q)])
    else:
        result.append(str(key_name[q]))

print('\n'.join(result))