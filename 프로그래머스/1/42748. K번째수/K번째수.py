def solution(array, commands):
    l = []
    for command in commands:
        i,j,k = command[0]-1,command[1],command[2]-1
        pick = array[i:j]
        pick.sort()
        l.append(pick[k])
    return l