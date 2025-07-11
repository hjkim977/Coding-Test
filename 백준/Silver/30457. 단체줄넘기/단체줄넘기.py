n = int(input())
students = list(map(int,input().split()))
students.sort()

left = [0]
right = [0]

for s in students:
    while s not in left or s not in right:
        if s not in left and left[-1]<s:
            left.append(s)
            break
        if s not in right and right[-1]<s:
            right.append(s)
            break
print(len(left)+len(right)-2)