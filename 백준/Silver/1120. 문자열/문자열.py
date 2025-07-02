x,y = input().split()
min_diff = float('inf')

for i in range(len(y)-len(x)+1):
    size = len(x)
    slice_y = y[i:i+size]
    diff = 0
    for j in range(len(slice_y)):
        if x[j]!=slice_y[j]:
            diff += 1
    min_diff = min(min_diff,diff)
print(min_diff)