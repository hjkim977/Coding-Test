def solution(wallpaper):
    a = len(wallpaper)
    b = len(wallpaper[0])
    
    min_x, min_y = a, b
    max_x, max_y = 0, 0
    
    for i in range(a):
        for j in range(b):
            if wallpaper[i][j] == "#":
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i)
                max_y = max(max_y, j)
    return [min_x,min_y,max_x+1,max_y+1]